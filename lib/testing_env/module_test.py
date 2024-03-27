import requests
import pytest

def requests_version():
    return requests.__version__

def pytest_version():
    return pytest.__version__

def test_requests_version():
    assert requests_version() == "2.27.1"

def test_pytest_version():
    assert pytest_version() == "7.1.3"
