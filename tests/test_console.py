"""Test cases for the console module."""
from unittest.mock import mock_open, patch

import click.testing
import pytest

from render_cli import console
from . import test_constants


class TestConsole:
    """Test console."""

    @pytest.fixture
    def runner(self):
        """Fixture for invoking command-line interfces."""
        return click.testing.CliRunner()

    @pytest.fixture(scope="class")
    def fetch_services_response(self):
        """Fixture for fetching services."""
        return test_constants.fetch_services_response

    @pytest.mark.e2e
    def test_main_succeeds(self, runner):
        """It exits with a status code of zero."""
        result = runner.invoke(console.cli)
        assert result.exit_code == 0

    def test_list_services_command(self, runner, fetch_services_response):
        """Tests console call to fetch-services command."""
        with patch("render_cli.console.rs") as mock_render_services:
            mock_render_services.fetch_services.return_value = (
                test_constants.test_services
            )
            # test verbose mode
            result = runner.invoke(console.cli, ["list", "-v"])
            assert result.exit_code == 0

            # test normal mode
            result = runner.invoke(console.cli, ["list"])
            assert result.exit_code == 0

    def test_find_service_command(self, runner):
        """Test console call to find_service_by_name."""
        with patch("render_cli.console.rs") as mock_render_services:
            mock_render_services.find_service_by_name.return_value = (
                test_constants.test_svc_1
            )
            # test verbose mode
            result = runner.invoke(
                console.cli, ["find-service", "-sn", "test-service-name", "-v"]
            )
            assert result.exit_code == 0

            # test normal mode
            result = runner.invoke(
                console.cli, ["find-service", "-sn", "test-service-name"]
            )
            assert result.exit_code == 0

    def test_list_env_command(self, runner):
        """Test console call fetch env vars for a service."""
        with patch("render_cli.console.rs") as mock_render_services:
            mock_render_services.find_service_by_name.return_value = (
                test_constants.test_svc_1
            )
            mock_render_services.retrieve_env_from_render.return_value = (
                test_constants.test_render_env_vars
            )

            # test verbose mode
            result = runner.invoke(
                console.cli, ["list-env", "-sn", "test-service-name", "-v"]
            )
            assert result.exit_code == 0

            # test normal mode
            result = runner.invoke(
                console.cli, ["list-env", "-sn", "test-service-name"]
            )
            assert result.exit_code == 0

    def test_set_env_command(self, runner):
        """Test console cli call to set env vars for a service."""
        with patch("os.path.isfile") as mock_isfile:
            mock_isfile.return_value = True
            file_data = mock_open(read_data=test_constants.test_file_with_comments)
            with patch("render_cli.utils.open", file_data):
                with patch("render_cli.utils") as mock_utils:
                    mock_utils.convert_env_var_file.return_value = (
                        test_constants.test_env_vars
                    )
                    with patch("render_cli.console.rs") as mock_render_services:
                        mock_render_services.find_service_by_name.return_value = (
                            test_constants.test_svc_1
                        )
                        mock_render_services.retrieve_env_from_render.return_value = (
                            test_constants.test_render_env_vars
                        )
                        mock_render_services.set_env_variables_for_service.return_value = (
                            ""
                        )
                        result = runner.invoke(
                            console.cli,
                            [
                                "set-env",
                                "-sn",
                                "test-service-name",
                                "-f",
                                "envfile.txt",
                            ],
                        )
                        assert result.exit_code == 0
