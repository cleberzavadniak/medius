def test_init(medius_client):
    assert medius_client.access_token == 'ACCESS_TOKEN'
    assert medius_client.mocked_request_method.called_once()
    assert medius_client.mocked_request_method.call_args[0][0] == 'https://api.medium.com/v1/me'
    assert medius_client.user_id == 'ID'
    assert medius_client.username == 'USERNAME'


def test_default_kwargs(medius_client):
    assert 'user_id' in medius_client.default_kwargs
    assert medius_client.default_kwargs['user_id'] == 'ID'


def test_get_current_user(medius_client):
    response = medius_client.get_current_user()
    assert response['id'] == 'ID'
    assert response['username'] == 'USERNAME'


def test_get_posts(medius_client):
    response = medius_client.get('posts')

    assert 'posts' in response.data
    assert len(response.data['posts']) == 1

    assert medius_client.mocked_request_method.call_args[0][0] == 'https://api.medium.com/v1/users/ID/posts'


def test_create_post(medius_client, post_payload):
    medius_client.post('posts', post_payload)

    expected_content = '<h1>{}</h1>{}'.format(post_payload['title'], post_payload['content'])
    assert medius_client.mocked_request_method.call_args[1]['json']['content'] == expected_content
    assert medius_client.mocked_request_method.call_args[0][0] == 'https://api.medium.com/v1/users/ID/posts'


def test_create_post_into_publication(medius_client, post_payload):
    medius_client.post_into_publication('PUBLICATION', post_payload)

    expected_content = '<h1>{}</h1>{}'.format(post_payload['title'], post_payload['content'])
    assert medius_client.mocked_request_method.call_args[1]['json']['content'] == expected_content
    assert medius_client.mocked_request_method.call_args[0][0] == 'https://api.medium.com/v1/publications/PUBLICATION_ID/posts'
