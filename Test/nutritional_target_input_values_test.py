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


class NutritionalTargetsValuesTest(unittest.TestCase):
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



    def test_adjust_invalid_macros(self):
        self.nutritional_targets_page.go_to_create_target()
        for target in self.INVALID_TARGETS:
            self.create_targets_page = CreateNutritionalTargetPage(self.driver)

            self.create_targets_page.adjust_macros(title=target["title"], calories=target["calories"],
                                                   fiber=target["fiber"], max_fats=target["max_fats"],
                                                   min_fats=target["min_fats"],
                                                   min_carbs=target['min_carbs'],
                                                   max_carbs=target['max_carbs'],
                                                   max_proteins=target['max_proteins'],
                                                   min_proteins=target['min_proteins'])
            min_max_carbs = self.create_targets_page.get_min_max_carbs()
            min_max_fats = self.create_targets_page.get_min_max_fats()
            min_max_proteins = self.create_targets_page.get_min_max_proteins()
            self.assertLessEqual(target['calories'],
                                 calculate_macro_calories(min_max_proteins[1], min_max_fats[1], min_max_carbs[1]))
            self.assertGreaterEqual(target['calories'],
                                    calculate_macro_calories(min_max_proteins[0], min_max_fats[0], min_max_carbs[0]))
            self.create_targets_page.clear_all_inputs()


    def tearDown(self):
        self.browser_wrapper.close_browser()
