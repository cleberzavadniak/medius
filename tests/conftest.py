from unittest.mock import Mock

import pytest

from medius.client import Client


@pytest.fixture
def medius_client():
    mocked_method = Mock(return_value=Mock(json=Mock(return_value={
        'data': {
            'id': 'ID',
            'username': 'USERNAME',
            'title': 'TITLE',
            'posts': [{'id': 'POST_ID', 'title': 'POST_TITLE'}]
        }
    })))

    Client.requests_methods['GET'] = mocked_method
    Client.requests_methods['POST'] = mocked_method
    Client.requests_methods['PATCH'] = mocked_method
    Client.requests_methods['DELETE'] = mocked_method
    Client.mocked_request_method = mocked_method

    c = Client('ACCESS_TOKEN')
    c._publications = {'PUBLICATION': {'id': 'PUBLICATION_ID', 'name': 'PUBLICATION'}}
    return c


@pytest.fixture
def post_payload():
    return {
        'title': 'TITLE',
        'content': 'CONTENT',
        'tags': ['TAG1', 'TAG2']
    }
