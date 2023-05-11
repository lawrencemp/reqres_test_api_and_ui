import pytest
from selenium import webdriver
from apis.reqres_api import ApiClient


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def api_calling():
    return ApiClient
