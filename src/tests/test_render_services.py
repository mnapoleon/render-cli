import json

import pytest

from renderctl.render_services import fetch_services
import renderctl.render_services


@pytest.fixture()
def fake_render_services():
    with open("fetch_services.json") as f:
        return json.load(f)


@pytest.fixture
def mock_requests_get(mocker):
    fake_resp = mocker.Mock()
    fake_resp.json = mocker.Mock(return_value=fake_render_services)
    # fake_resp.status_code = HTTPStatus.OK

    mock = mocker.patch("fetch_services.requests.get", return_value=fake_resp)
    return mock


def test_get_requests(mock_requests_get):
    result = renderctl.render_services.fetch_services()
    assert "svc-1234566" == result["service"]["id"]
