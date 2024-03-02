import time
from telnetlib import EC

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import *

from Infra.base_page import BasePage


class PlannerPage(BasePage):
    EDIT_DAY_BUTTON = (By.XPATH, "//button[./span[contains(text(),'Edit')]]")
    GENERATE_BUTTON = (By.XPATH, "//button[./span[contains(text(),'Generate')]]")
    MEALS_TITLE = (By.XPATH, "//h2[contains(text(),'Meals')]")
    CALORIES = (By.XPATH, "//th[text()='Calories']/following-sibling :: td")
    REGENERATE = (By.XPATH, "//button[@title='Regenerate Day']")
    REGENERATE_POPUP_BUTTON=(By.XPATH,"//button[@class='_interaction_11et8_1 primary svelte-1m78l37']")

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
        self.regen_button = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(self.REGENERATE))

    def init_calories(self):
        self.calories = self._driver.find_elements(*self.CALORIES)

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

        self.add_food_button=WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, formated_string_locator)))

    def is_edit_day_button_active(self):
        return 'active' in self.edit_day.get_attribute("class")

    def click_add_food_to_meal_button(self, meal):
        self.init_edit_day_button()
        if not self.is_edit_day_button_active():
            self.edit_day.click()

        self.init_add_food_button(meal)
        self.add_food_button.click()

    def get_total_calories(self):
        time.sleep(1)
        self.init_calories()
        return self.calories[0].text

    def is_meal_generated(self):
        if len(self._driver.find_elements(*self.GENERATE_BUTTON)) > 0:
            return False
        return True

    def regenerate_meal_plan(self):
        self.regen_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(self.REGENERATE))
        self.regen_button.click()
        WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(self.REGENERATE_POPUP_BUTTON)).click()
