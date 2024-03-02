import time
from telnetlib import EC

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from Utils.urls import urls
from Infra.base_page import BasePage
from Logic.create_nutritional_target_page import CreateNutritionalTargetPage


class NutritionalTargetPage(BasePage):
    CREATE_TARGET_BUTTON = (By.XPATH, "//a[./span[text()='Create ']]")
    ALL_TARGET_TITLES = (By.XPATH, "//header[@class='svelte-10kr2ij']/h3")
    TARGETS = (By.XPATH,"//article[@class='_interaction_11et8_1 svelte-1cvve7m horizontal']")
    DELETE_TARGET =(By.XPATH,"//button[./span[contains(text(),'Delete')]]")
    DELETE_DIALOG = (By.XPATH,"//dialog//button[@class='_interaction_11et8_1 primary svelte-1m78l37']")

    def __init__(self, driver):
        super().__init__(driver)
        self._driver.get(urls['Nutritional_Target'])
        self.init_elements()

    def init_elements(self):
        self.target_button = self.wait_for_element_in_page_by_xpath(self.CREATE_TARGET_BUTTON[1])

    def init_targets(self):
        time.sleep(3)
        self.wait_for_element_in_page_by_xpath(self.TARGETS[1])
        self.target_titles = self._driver.find_elements(*self.ALL_TARGET_TITLES)
        self.tagets = self._driver.find_elements(*self.TARGETS)

    def create_nurtional_target(self, title, calories, fiber, min_carbs, max_carbs, min_fats, max_fats,
                                min_proteins, max_proteins):
        self.wait_for_element_in_page_by_xpath(self.CREATE_TARGET_BUTTON[1]).click()
        self.create_target = CreateNutritionalTargetPage(self._driver)
        self.create_target.fill_nutritional_target_inputs(title, calories, fiber, min_carbs, max_carbs, min_fats,
                                                          max_fats,
                                                          min_proteins, max_proteins)
        self.create_target.save_target()

    def go_to_create_target(self):
        self.init_elements()
        self.target_button.click()

    def get_target_titles(self):
        self.init_targets()
        all_title = []
        for title in self.target_titles:
            all_title.append(title.text)
        return all_title
    def delete_last_target(self):
        self.init_targets()
        self.tagets[len(self.tagets)-1].click()
        self.wait_for_element_in_page_by_xpath(self.DELETE_TARGET[1]).click()
        self.wait_for_element_in_page_by_xpath(self.DELETE_DIALOG[1]).click()