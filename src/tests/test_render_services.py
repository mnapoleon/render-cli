import unittest
from unittest.mock import patch, MagicMock, Mock

from renderctl.render_services import \
    fetch_services, create_headers, \
    find_service_by_name, retrieve_env_from_render
from . import test_constants


class TestRenderServices(unittest.TestCase):

    @patch('renderctl.render_services.requests')
    def test_get_requests(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = test_constants.test_services
        mock_requests.get.return_value.__enter__.return_value = mock_response

        result = fetch_services()
        s_id = result[0]['service']['id']
        assert "srv-cc3vjrhgp3jqnl0xxxxx" == s_id

    @patch('renderctl.render_services.requests')
    def test_find_service_by_name(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = test_constants.test_services
        mock_requests.get.return_value.__enter__.return_value = mock_response

        result = find_service_by_name('render-service-name-1')
        assert result == test_constants.test_svc_1

    @patch('renderctl.render_services.requests')
    def test_retrieve_env_from_render(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = test_constants.test_env_vars
        mock_requests.get.return_value.__enter__.return_value = mock_response

        result = retrieve_env_from_render('service-id')
        assert len(result) == 4
        assert result[0] == test_constants.test_env_var_1
        assert result[1] == test_constants.test_env_var_2
        assert result[2] == test_constants.test_env_var_3
        assert result[3] == test_constants.test_env_var_4


    @patch('renderctl.render_services.os')
    def test_create_headers(self, mock_os):
        mock_os.getenv.return_value = "mock_token_1234"

        headers_for_get = create_headers()
        assert headers_for_get['Accept'] == 'application/json'
        assert headers_for_get['Authorization'] == 'Bearer mock_token_1234'

        headers_for_post = create_headers(is_post=True)
        assert headers_for_post['Accept'] == 'application/json'
        assert headers_for_post['Content-Type'] == 'application/json'
        assert headers_for_post['Authorization'] == 'Bearer mock_token_1234'
