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
from logic.weight_goal_page import WeightGoalPage


class WeightGoalTest(unittest.TestCase):
    VALID_TARGETS = valid_targets
    INVALID_TARGETS = invalid_target
    USER = get_valid_user('Hosam')

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.get_driver(browser=self.__class__.browser)
        self.login_page = LoginPage(self.driver)
        self.login_page.login_with_email_password(self.USER['email'], self.USER['password'])
        time.sleep(2)
        self.weight_goals_page = WeightGoalPage(self.driver)

    def test_invalid_weight_input_negative(self):
        self.weight_goals_page.update_weight(-1)
        self.assertEqual(self.weight_goals_page.get_validation_message(),['Value must be greater than or equal to 0.','Please select a value that is no less than 0.'])

    def test_invalid_weight_input_greater_than_upper_limit(self):
        self.weight_goals_page.update_weight(1000)
        self.assertTrue(self.weight_goals_page.get_validation_message(),['Value must be less than or equal to 999.','Please select a value that is no more than 999.'])

    def test_valid_weight_input(self):
        weight = 80
        self.weight_goals_page.update_weight(weight)
        self.assertIn(str(weight),self.weight_goals_page.get_last_updated_label())
        weight= 100
        self.weight_goals_page.update_weight(weight)
        self.assertIn(str(weight),self.weight_goals_page.get_last_updated_label())



    def tearDown(self):
        self.browser_wrapper.close_browser()
