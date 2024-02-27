import time
from telnetlib import EC

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import *

from infra.base_page import BasePage


class PlannerPage(BasePage):
    EDIT_DAY_BUTTON = (By.XPATH, "//button[./span[contains(text(),'Edit')]]")
    GENERATE_BUTTON = (By.XPATH, "//button[./span[contains(text(),'Generate')]]")
    MEALS_TITLE = (By.XPATH, "//h2[contains(text(),'Meals')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.generate_page()
        self.init_elements()

    def generate_page(self):
        self.generate_button = None

        if not self.is_meal_generated():
            self.generate_button = self._driver.find_element(*self.GENERATE_BUTTON)
            try:
                WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(self.GENERATE_BUTTON)).click()
                self.wait_for_element_in_page_by_xpath(self.MEALS_TITLE)
            except:
                ElementNotInteractableException("can't click on Generate button")
                NoSuchElementException("clicking on generate button didnt's generate a meal plan")

    def init_elements(self):
        self.init_edit_day_button()

    def init_edit_day_button(self):
        self.wait_for_element_in_page_by_xpath(self.EDIT_DAY_BUTTON[1])
        try:
            WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(self.EDIT_DAY_BUTTON))
        except:
            ElementNotInteractableException("can't click on ''Edit Day")
        self.edit_day = self._driver.find_element(*self.EDIT_DAY_BUTTON)

    def add_food_button_by_meal_locator(self, meal):
        return f"//section[./header[./h3[contains(text(),'{meal}')]]]//button[./span[contains(text(),'Add Food')]]"

    def init_add_food_button(self, meal):
        formated_string_locator = self.add_food_button_by_meal_locator(meal)
        if meal not in ('Breakfast', 'Dinner', 'Lunch', 'Snack'):
            raise ValueError("invalid meal name input should be 'breakfast','dinner','lunch' or 'snack'")
        try:
            self.wait_for_element_in_page_by_xpath(formated_string_locator)

            WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(self.add_food_button))

        except:
            NoSuchElementException(f"add button for meal {meal} not found")
            ElementNotInteractableException("can't click on add food button")

        self.add_food_button = self._driver.find_element(By.XPATH, formated_string_locator)

    def is_edit_day_button_active(self):
        return 'active' in self.edit_day.get_attribute("class")

    def click_add_food_to_meal_button(self, meal):
        self.init_edit_day_button()
        if not self.is_edit_day_button_active():
            self.edit_day.click()

        self.init_add_food_button(meal)
        self.add_food_button.click()

    def is_meal_generated(self):
        if len(self._driver.find_elements(*self.GENERATE_BUTTON)) > 0:
            return False
        return True
