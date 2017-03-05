import requests
from json.decoder import JSONDecodeError


class MethodNotAllowed(Exception):
    pass


def post_transformation(data):
    data['content'] = '<h1>{title}</h1>{content}'.format(**data)
    return data


class Client:
    base_url = 'https://api.medium.com/v1/'

    resources = {
        'me': {
            'path': 'me',
            'methods': ['GET'],
        },
        'posts': {
            'path': 'users/{user_id}/posts',
            'data': {
                'contentFormat': 'html',
                'publishStatus': 'draft',
                'notifyFollowers': False,
            },
            'transformation': post_transformation,
        },
        'publication_posts': {
            'path': 'publications/{publication_id}/posts',
            'data': {
                'contentFormat': 'html',
                'publishStatus': 'draft',
                'notifyFollowers': False,
            },
            'transformation': post_transformation,
        },
        'publications': {
            'path': 'users/{user_id}/publications',
        }
    }

    requests_methods = {
        'GET': requests.get,
        'POST': requests.post,
        'PATCH': requests.patch,
        'DELETE': requests.delete,
    }

    default_kwargs = {}

    def __init__(self, access_token):
        self._publications = None

        self.access_token = access_token

        self.headers = {'Authorization': 'Bearer {}'.format(access_token)}

        self.user = self.get_current_user()

        self.user_id = self.user['id']
        self.username = self.user['username']

        self.default_kwargs['user_id'] = self.user_id

    def get_current_user(self):
        response = self.get('me')
        response.raise_for_status()

        return response.data

    def _request(self, method, resource_name, data=None, **kwargs):
        resource = self.resources[resource_name]
        allowed_methods = resource.get('methods', ['GET', 'POST', 'PATCH', 'DELETE'])
        if method not in allowed_methods:
            raise MethodNotAllowed('The resource "{}" does not allow the method {}'.format(resource_name, method))

        format_args = dict(self.default_kwargs)
        format_args.update(kwargs)
        path = self.base_url + (resource['path'].format(**format_args))

        requests_method = self.requests_methods[method]

        request_data = resource.get('data', {})
        request_data.update(data or {})

        if method not in ('GET', 'DELETE'):
            transformation = resource.get('transformation', None)
            if transformation is not None:
                request_data = transformation(request_data)

        response = requests_method(path, json=request_data, headers=self.headers)

        try:
            response_data = response.json()
        except JSONDecodeError:
            response.data = {}
        else:
            response_data_data = response_data.get('data', None)
            if response_data_data is not None:
                response.data = response_data_data
            else:
                response.data = response_data

        return response

    def get(self, resource_name, **kwargs):
        return self._request('GET', resource_name, **kwargs)

    def post(self, resource_name, data, **kwargs):
        return self._request('POST', resource_name, data=data, **kwargs)

    def patch(self, resource_name, data, **kwargs):
        return self._request('patch', resource_name, data=data, **kwargs)

    def delete(self, resource_name, **kwargs):
        return self._request('DELETE', resource_name, **kwargs)

    @property
    def publications(self):
        if self._publications is None:
            response = self.get('publications')
            self._publications = {p['name']: p for p in response.data}

        return self._publications

    def post_into_publication(self, publication_name, post_data):
        return self.post('publication_posts', post_data, publication_id=self.publications[publication_name]['id'])
