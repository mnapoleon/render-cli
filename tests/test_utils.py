"""Tests for utils.py."""
from unittest import mock

import render_cli.utils as utils
from . import test_constants


@mock.patch("os.path.isfile")
def test_convert_env_var_file(mock_isfile):
    """Tests converting env var file to dict."""
    mock_isfile.return_value = True
    file_data = mock.mock_open(read_data=test_constants.test_file_with_comments)
    with mock.patch("render_cli.utils.open", file_data):
        assert test_constants.test_env_vars_missing_key3 == utils.convert_env_var_file(
            "any.txt"
        )


def test_convert_from_render_env_format():
    """Tests converting render env output to dict."""
    result = utils.convert_from_render_env_format(test_constants.test_render_env_vars)
    assert result == test_constants.test_env_var_dict


def test_convert_to_render_env_format():
    """Tests converting dict to render env format."""
    assert (
        utils.convert_to_render_env_format(test_constants.test_env_vars)
        == test_constants.test_env_var_render_format
    )
