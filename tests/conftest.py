import pytest


@pytest.fixture
def mock_requests_get(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "Lorem ipsum dolor sit amet",
    }
    return mock

# The hook is placed in the conftest.py file, at the top-level of your tests
# package. This ensures that Pytest can # discover the module and use it for
# the entire test suite.


def pytest_configure(config):
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")
