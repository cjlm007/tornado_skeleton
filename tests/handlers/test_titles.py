import httplib

import pytest
from doubles import allow_constructor, expect, patch_class

from bootcamp.services.title_service import TitleService


@pytest.fixture
def gen_mock_service():
    class_name = 'bootcamp.handlers.titles.TitleService'
    mock_service = TitleService()
    service_class = patch_class(class_name)
    allow_constructor(service_class).and_return(mock_service)
    return mock_service


@pytest.mark.gen_test
def test_titles(http_client, base_url):
    mock_service = gen_mock_service()
    expect(mock_service).get_titles.and_return_future([])

    response = yield http_client.fetch(base_url + '/titles')
    assert response.body == 'Number of titles: 0'
    assert response.code == httplib.OK
