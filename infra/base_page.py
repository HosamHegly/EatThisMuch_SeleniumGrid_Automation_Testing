from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage():
    def __init__(self, driver):
        self._driver = driver

    def wait_for_element_in_page_by_xpath(self, path):
        return WebDriverWait(self._driver, 10).until(lambda x: x.find_element(By.XPATH, path))

    def wait_for_element_in_page_by_CSS(self, path):
        return WebDriverWait(self._driver, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, path))

    def get_current_url(self):
        return self._driver.current_url
    def get_title(self):
        return self._driver.title
