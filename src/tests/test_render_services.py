import unittest
from unittest.mock import patch, MagicMock, Mock

from renderctl.render_services import fetch_services, create_headers


class TestRenderServices(unittest.TestCase):


    @patch('renderctl.render_services.requests')
    def test_get_requests(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{
            "cursor": "eMHLdAJXBHZqcmhncDNqcW5sMHF1Z29n",
            "service": {
                "id": "srv-cc3vjrhgp3jqnl0xxxxx",
                "name": "render-service-name",
                "serviceDetails": {
                    "url": "https://render-service-name.onrender.com"
                }
            }
        }]
        mock_requests.get.return_value.__enter__.return_value = mock_response

        result = fetch_services()
        s_id = result[0]['service']['id']
        assert "srv-cc3vjrhgp3jqnl0xxxxx" == s_id

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