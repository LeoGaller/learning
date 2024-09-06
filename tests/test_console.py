# tests/test_console.py
import click.testing
import pytest
from unittest.mock import Mock
from click.testing import CliRunner
from pytest_mock import MockFixture

from hypermodern_python import console

@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_succeeds(runner: CliRunner, mock_requests_get: Mock) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(console.main)
    assert result.exit_code == 0


@pytest.fixture
def mock_requests_get(mocker: MockFixture) -> Mock:
    """Fixture for mocking requests.get."""
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "Lorem ipsum dolor sit amet",
    }
    return mock

def test_main_prints_title(runner, mock_requests_get):
    """check that the title returned by the API is printed to the console"""
    result = runner.invoke(console.main)
    assert "Lorem Ipsum" in result.output

def test_main_uses_en_wikipedia_org(runner, mock_requests_get):
    """Mock objects also allow you to inspect the arguments they were called with, using the call_args attribute.
    This allows you to check the URL passed to requests.get """
    runner.invoke(console.main)
    args, _ = mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]

def test_main_fails_on_request_error(runner, mock_requests_get):
    """You can configure a mock to raise an exception instead of returning a value by assigning the exception instance
    or class to the side_effect attribute of the mock.  """
    mock_requests_get.side_effect = Exception("Boom")
    result = runner.invoke(console.main)
    assert result.exit_code == 1