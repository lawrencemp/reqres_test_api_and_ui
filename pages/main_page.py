from pages.base_page import BasePage
from pages.locators import MainPageLocators
from selenium.webdriver.common.by import By
from apis.reqres_api import ApiClient
from json import loads


class MainPage(BasePage):
    def find_method(self, request_locator):
        return self.get_element(*request_locator).get_attribute("data-http")

    def scroll_into_requests(self):
        elem = self.browser.find_element(*MainPageLocators.SECTION_WITH_ENDPOINTS)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", elem)

    def is_all_endpoint_elements_are_visible(self, method, request_locator):
        if method == 'get' or method == 'delete':
            assert self.is_element_present(*request_locator) and self.is_element_present(
                *MainPageLocators.REQUEST_URL) \
                   and self.is_element_present(*MainPageLocators.RESPONSE_CODE) \
                   and self.is_element_present(*MainPageLocators.OUTPUT_RESPONSE), "Не все поля запроса отображены"
        else:
            assert self.is_element_present(*request_locator) and self.is_element_present(
                *MainPageLocators.REQUEST_URL) \
                   and self.is_element_present(*MainPageLocators.RESPONSE_CODE) \
                   and self.is_element_present(*MainPageLocators.OUTPUT_RESPONSE) \
                   and self.is_element_present(*MainPageLocators.OUTPUT_REQUEST), "Не все поля запроса отображены"

    def get_api_response(self, method):
        if method == 'get' or method == 'delete':
            path = self.get_element(*MainPageLocators.REQUEST_URL).text
            if method == 'get':
                return ApiClient.get_reqres(self.url, path)
            else:
                return ApiClient.delete_reqres(self.url, path)
        else:
            path = self.get_element(*MainPageLocators.REQUEST_URL).text
            body = loads(self.get_element(*MainPageLocators.OUTPUT_REQUEST).text.replace("\n", ""))
            if method == 'post':
                return ApiClient.post_reqres(self.url, path, body)
            elif method == 'patch':
                return ApiClient.patch_reqres(self.url, path, body)
            else:
                return ApiClient.put_reqres(self.url, path, body)

    def is_api_response_equal(self, method):
        api_response = self.get_api_response(method)
        ui_status_code = self.get_element(*MainPageLocators.RESPONSE_CODE).text
        assert str(api_response.status_code) == ui_status_code, "Коды ответа не совпадают"
        if method != 'delete':
            ui_response_body = loads(self.get_element(*MainPageLocators.OUTPUT_RESPONSE).text)
            api_response_dict = api_response.json()
            if method == 'get':
                assert api_response_dict == ui_response_body, "Тела ответа не совпадают"
            else:
                assert api_response_dict.keys() == ui_response_body.keys(), "Поля ответов не совпадают"
