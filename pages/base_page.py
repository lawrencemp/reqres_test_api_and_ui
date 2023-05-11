from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def get_element(self, how, what, timeout=4):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))

    def scroll_into_element(self, how, what):
        elem = self.browser.find_element(how, what)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", elem)

    def is_element_present(self, how, what, timeout=6):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
            return False
        return True
