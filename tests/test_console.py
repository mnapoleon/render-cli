"""Test cases for the console module."""
import click.testing
import pytest


from render_cli import console


@pytest.fixture
def runner():
    """Fixture for invoking command-line interfces."""
    return click.testing.CliRunner()


@pytest.mark.e2e
def test_main_succeeds(runner):
    """It exits with a status code of zero."""
    result = runner.invoke(console.cli)
    assert result.exit_code == 0
