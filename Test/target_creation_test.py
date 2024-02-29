import concurrent.futures.thread
import time

import selenium
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import unittest
import json

from Utils.helper_functions import calculate_macro_calories
from infra.browser_wrapper import BrowserWrapper
from logic.create_nutritional_target_page import CreateNutritionalTargetPage
from logic.food_search_popup import FoodSearchPopup
from logic.login_page import LoginPage
from logic.menu import Menu
from logic.nutritional_target_page import NutritionalTargetPage
from logic.planner_page import PlannerPage
from Utils.calorie_target import *
from Utils.users import *


class CreateTargetTest(unittest.TestCase):
    VALID_TARGETS = valid_targets
    INVALID_TARGETS = invalid_target
    USER = get_valid_user('Hosam')

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.get_driver(browser=self.__class__.browser)
        self.login_page = LoginPage(self.driver)
        self.login_page.login_with_email_password(self.USER['email'], self.USER['password'])
        time.sleep(2)
        self.nutritional_targets_page = NutritionalTargetPage(self.driver)

    import concurrent.futures.thread
    import time

    import selenium
    from selenium import webdriver
    from selenium.webdriver import Keys
    from selenium.webdriver.common.by import By
    import unittest
    import json

    from Utils.helper_functions import calculate_macro_calories
    from infra.browser_wrapper import BrowserWrapper
    from logic.create_nutritional_target_page import CreateNutritionalTargetPage
    from logic.food_search_popup import FoodSearchPopup
    from logic.login_page import LoginPage
    from logic.menu import Menu
    from logic.nutritional_target_page import NutritionalTargetPage
    from logic.planner_page import PlannerPage
    import Utils.calorie_target
    import Utils.users

class CreateNutritionalTargetsTest(unittest.TestCase):
    _non_parallel = True
    VALID_TARGETS = valid_targets
    INVALID_TARGETS = invalid_target
    USER = get_valid_user('Hosam')

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.get_driver(browser=self.__class__.browser)
        self.login_page = LoginPage(self.driver)
        self.login_page.login_with_email_password(self.USER['email'], self.USER['password'])
        time.sleep(2)
        self.nutritional_targets_page = NutritionalTargetPage(self.driver)

    def test_create_valid_nutritional_target(self):
        for target in self.VALID_TARGETS:
            self.nutritional_targets_page.create_nurtional_target(title=target["title"], calories=target["calories"],
                                                                  fiber=target["fiber"], max_fats=target["max_fats"],
                                                                  min_fats=target["min_fats"],
                                                                  min_carbs=target['min_carbs'],
                                                                  max_carbs=target['max_carbs'],
                                                                  max_proteins=target['max_proteins'],
                                                                  min_proteins=target['min_proteins'])
            self.assertIn(target["title"], self.nutritional_targets_page.get_target_titles())


    def tearDown(self):
        self.nutritional_targets_page.delete_last_target()
        self.browser_wrapper.close_browser()
