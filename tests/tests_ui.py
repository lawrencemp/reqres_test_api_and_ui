import pytest
from selenium.webdriver.common.by import By
from utils.locators_for_parametrize import get_all_li_elements
from pages.main_page import MainPage


@pytest.mark.ui_test
class TestUi:
    HOST = 'https://reqres.in'

    @pytest.mark.parametrize("request_locator", get_all_li_elements())
    def test_ui_request(self, browser, request_locator: tuple[str, str]):
        page = MainPage(browser, self.HOST)
        page.open()
        page.scroll_into_requests()
        page.get_element(*request_locator).click()
        method = page.find_method(request_locator)
        page.is_all_endpoint_elements_are_visible(method, request_locator)
        page.is_api_response_equal(method)
