import time
from telnetlib import EC

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *

from infra.base_page import BasePage



class LoginPage(BasePage):
    EMAIL_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.XPATH, "//input[@autocomplete='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)
        self.init_elements()

    def init_elements(self):
        self.email_field = self._driver.find_element(*self.EMAIL_FIELD)
        self.password_field = self._driver.find_element(*self.PASSWORD_FIELD)
        self.login_button = self._driver.find_element(*self.LOGIN_BUTTON)

    def fill_email_field(self, email):
        self.email_field.send_keys(email)

    def fill_password_field(self, password):
        self.password_field.send_keys(password)

    def login_with_email_password(self, email, password):
        self.fill_email_field(email)
        self.fill_password_field(password)
        self.login_button.click()
