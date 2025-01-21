# tests/test_console.py
import click.testing
import pytest
from unittest.mock import Mock
from click.testing import CliRunner
import requests
from hypermodern_python import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_succeeds(runner: CliRunner, mock_requests_get: Mock) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_prints_title(runner, mock_requests_get):
    """check that the title returned by the API is printed to the console"""
    result = runner.invoke(console.main)
    assert "Lorem Ipsum" in result.output


def test_main_uses_en_wikipedia_org(runner, mock_requests_get):
    """Mock objects also allow you to inspect the arguments they were called
    with, using the call_args attribute. This allows you to check the URL
    passed to requests.get """
    runner.invoke(console.main)
    args, _ = mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]


def test_main_fails_on_request_error(runner, mock_requests_get):
    """You can configure a mock to raise an exception instead of returning a
    value by assigning the exception instance
    or class to the side_effect attribute of the mock.  """
    mock_requests_get.side_effect = Exception("Boom")
    result = runner.invoke(console.main)
    assert result.exit_code == 1


def test_main_prints_message_on_request_error(runner, mock_requests_get):
    """configuring the mock to raise a RequestException"""
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output


@pytest.fixture
def mock_wikipedia_random_page(mocker):
    return mocker.patch("hypermodern_python.wikipedia.random_page")


def test_main_uses_specified_language(runner, mock_wikipedia_random_page):
    runner.invoke(console.main, ["--language=pl"])
    mock_wikipedia_random_page.assert_called_with(language="pl")


@pytest.mark.e2e
def test_main_succeeds_in_production_env(runner):
    """ end-to-end tests """
    result = runner.invoke(console.main)
    assert result.exit_code == 0
