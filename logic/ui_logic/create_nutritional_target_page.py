from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.ui_infra.base_page import BasePage


class CreateNutritionalTargetPage(BasePage):
    TITLE = (By.XPATH, "//input[@name='title']")
    CALORIES = (By.XPATH, "//input[@id='calories']")
    FIBER = (By.XPATH, "//input[@id='fiber']")
    MIN_CARBS = (By.XPATH, "//input[@aria-label='Min Carbs']")
    MAX_CARBS = (By.XPATH, "//input[@aria-label='Max Carbs']")
    MIN_FATS = (By.XPATH, "//input[@aria-label='Min Fats']")
    MAX_FATS = (By.XPATH, "//input[@aria-label='Max Fats']")
    MIN_PROTEINS = (By.XPATH, "//input[@aria-label='Min Proteins']")
    MAX_PROTEINS = (By.XPATH, "//input[@aria-label='Max Proteins']")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    ADJUST_MACOS_BUTTON = (By.XPATH, "//button[./span[text()='Adjust macros']]")

    def __init__(self, driver):
        super().__init__(driver)

        self.init_elements()

    def init_elements(self):
        self.calories = self.wait_for_element_in_page_by_xpath(self.CALORIES[1])
        self.title = self._driver.find_element(*self.TITLE)
        self.fiber = self._driver.find_element(*self.FIBER)
        self.min_carbs = self._driver.find_element(*self.MIN_CARBS)
        self.max_carbs = self._driver.find_element(*self.MAX_CARBS)
        self.min_fats = self._driver.find_element(*self.MIN_FATS)
        self.max_fats = self._driver.find_element(*self.MAX_FATS)
        self.min_proteins = self._driver.find_element(*self.MIN_PROTEINS)
        self.max_proteins = self._driver.find_element(*self.MAX_PROTEINS)
        self.save_button = self._driver.find_element(*self.SAVE_BUTTON)

    def fill_nutritional_target_inputs(self, title, calories, fiber, min_carbs, max_carbs, min_fats, max_fats,
                                       min_proteins, max_proteins):
        self.clear_all_inputs()
        self.title.send_keys(title)
        self.calories.send_keys(calories)
        self.min_fats.send_keys(min_fats)
        self.max_fats.send_keys(max_fats)
        self.min_proteins.send_keys(min_proteins)
        self.max_proteins.send_keys(max_proteins)

        self.max_carbs.send_keys(max_carbs)
        self.min_carbs.send_keys(min_carbs)
        self.fiber.send_keys(fiber)
        self.save_button.click()

    def clear_all_inputs(self):
        self.fiber.clear()
        self.calories.clear()
        self.min_carbs.clear()
        self.min_fats.clear()
        self.min_proteins.clear()
        self.max_carbs.clear()
        self.max_fats.clear()
        self.max_proteins.clear()
        self.title.clear()

    def save_target(self):
        self.save_button.click()

    def init_adjust_macros(self):
        self.adjust_macros = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(self.ADJUST_MACOS_BUTTON))

    def adjust_macros(self, title, calories, fiber, min_carbs, max_carbs, min_fats, max_fats,
                      min_proteins, max_proteins):
        self.fill_nutritional_target_inputs(title, calories, fiber, min_carbs, max_carbs, min_fats, max_fats,
                                            min_proteins, max_proteins)
        self.init_adjust_macros()

        self.adjust_macros.click()

    def get_min_max_carbs(self):
        return int(self.min_carbs.get_attribute('value')), int(self.max_carbs.get_attribute('value'))

    def get_min_max_fats(self):
        return int(self.min_fats.get_attribute('value')), int(self.max_fats.get_attribute('value'))

    def get_min_max_proteins(self):
        return int(self.min_proteins.get_attribute('value')), int(self.max_proteins.get_attribute('value'))
