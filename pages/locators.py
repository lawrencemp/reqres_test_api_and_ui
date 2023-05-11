from selenium.webdriver.common.by import By


class BasePageLocators:
    pass


class MainPageLocators:
    SECTION_WITH_ENDPOINTS = (By.XPATH, '//section[@class="console try-api-links"]')
    USER_LIST_REQUEST = (By.XPATH, '//li[@data-id="users"]')
    USER_SINGLE_REQUEST = (By.XPATH, '//li[@data-id="users-single"]')
    USER_SINGLE_404_REQUEST = (By.XPATH, '//li[@data-id="users-single-not-found"]')
    PUT_REQUEST = (By.XPATH, '//li[@data-id="put"]')
    REQUEST_URL = (By.XPATH, '//span[@data-key="url"]')
    RESPONSE_CODE = (By.XPATH, '//span[@data-key="response-code"]')
    OUTPUT_RESPONSE = (By.XPATH, '//pre[@data-key="output-response"]')
    OUTPUT_REQUEST = (By.XPATH, '//pre[@data-key="output-request"]')
