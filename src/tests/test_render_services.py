import json
import unittest

import pytest
from unittest.mock import patch, MagicMock

from renderctl.render_services import fetch_services

services = [{
            "cursor": "eMHLdAJXBHZqcmhncDNqcW5sMHF1Z29n",
            "service": {"id": "srv-cc3vjrhgp3jqnl0qugog",
                        "name": "test-service-name"}
        }
        ]
class TestRenderServices(unittest.TestCase):

    @patch('renderctl.render_services.requests')
    def test_get_requests(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = services
        mock_requests.get.return_value = mock_response
        result = fetch_services()
        self.assertEqual(services, result)
