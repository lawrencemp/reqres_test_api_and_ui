from pages.locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium import webdriver


def get_all_li_elements():
    browser_ = webdriver.Chrome()
    browser_.get("https://reqres.in/")
    elem = browser_.find_element(*MainPageLocators.SECTION_WITH_ENDPOINTS)
    browser_.execute_script("arguments[0].scrollIntoView(true);", elem)
    li_elements = browser_.find_elements(By.XPATH, '//div[@data-key="endpoints"]//li')
    li_element_locators: list[tuple[str, str]] = []
    for li in li_elements:
        data_id = li.get_attribute("data-id")
        print(li.text)
        li_element_locators.append((By.XPATH, f'//div[@data-key="endpoints"]//li[@data-id="{data_id}"]'))
    browser_.quit()
    return li_element_locators
