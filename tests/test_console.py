"""Test cases for the console module."""
import click.testing
import pytest


from renderctl import console


@pytest.fixture
def runner():
    """Fixture for invoking command-line interfces."""
    return click.testing.CliRunner()


def test_main_succeeds(runner):
    """It exits with a status code of zero."""
    result = runner.invoke(console.cli)
    assert result.exit_code == 0
