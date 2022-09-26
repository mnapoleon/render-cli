from unittest.mock import patch, MagicMock, Mock

import pytest

from renderctl.render_services import(
    fetch_services, create_headers,
    find_service_by_name, retrieve_env_from_render,
    get_bearer_token)

import responses

from . import test_constants


class TestRenderServices:

    @pytest.fixture(scope="class")
    def fetch_services_response(self):
        return test_constants.fetch_services_response

    @pytest.fixture(scope="class")
    def fetch_services_failed_responses(self):
        return [
            test_constants.fetch_services_failed_with_401,
            test_constants.fetch_services_failed_with_406,
            test_constants.fetch_services_failed__with_429,
            test_constants.fetch_services_failed__with_500,
            test_constants.fetch_services_failed__with_503,
            test_constants.fetch_services_failed__with_402,
            ]

    @pytest.fixture(scope="class")
    def retrieve_env_vars_response(self):
        return test_constants.retrieve_env_vars_response

    @pytest.fixture(scope="class")
    def env_vars_failed_response(self):
        return test_constants.retrieve_env_vars_failed_with_401

    @responses.activate
    def test_fetch_services(self, fetch_services_response):
        responses.add(fetch_services_response)

        result = fetch_services()
        s_id = result[0]['service']['id']
        assert "srv-cc3vjrhgp3jqnl0xxxxx" == s_id

    @responses.activate
    def test_fetch_services_failure(self, fetch_services_failed_responses):
        for failure_response in fetch_services_failed_responses:
            responses.add(failure_response)
        result = fetch_services()
        assert result['error'] == '401 - Unauthorized'
        result = fetch_services()
        assert result['error'] == '406 - request error'
        result = fetch_services()
        assert result['error'] == '429 - Exceeded service limit'
        result = fetch_services()
        assert result['error'] == '500 - Render service unavailable'
        result = fetch_services()
        assert result['error'] == '503 - Render service unavailable'
        result = fetch_services()
        assert result['error'] == '402 - unexpected error'

    @responses.activate
    def test_find_service_by_name(self, fetch_services_response):
        responses.add(fetch_services_response)
        result = find_service_by_name('render-service-name-1')
        assert result == test_constants.test_svc_1

    @responses.activate
    def test_retrieve_env_from_render(self, retrieve_env_vars_response):
        responses.add(retrieve_env_vars_response)
        result = retrieve_env_from_render("service-id")
        assert result[0] == test_constants.test_env_var_1
        assert result[1] == test_constants.test_env_var_2
        assert result[2] == test_constants.test_env_var_3
        assert result[3] == test_constants.test_env_var_4

    @responses.activate
    def test_failure_retrieve_env_from_render(self, env_vars_failed_response):
        responses.add(env_vars_failed_response)
        result = retrieve_env_from_render('service-id')
        print(result)

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

    @patch('renderctl.render_services.os')
    def test_get_bearer_token(self, mock_os):
        mock_os.getenv.return_value = None
        assert get_bearer_token() is None
