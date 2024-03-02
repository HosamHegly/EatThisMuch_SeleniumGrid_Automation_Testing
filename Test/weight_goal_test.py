import concurrent.futures.thread
import time

import selenium
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import unittest
import json

from Utils.helper_functions import calculate_macro_calories
from Infra.browser_wrapper import BrowserWrapper
from Logic.create_nutritional_target_page import CreateNutritionalTargetPage
from Logic.food_search_popup import FoodSearchPopup
from Logic.login_page import LoginPage
from Logic.menu import Menu
from Logic.nutritional_target_page import NutritionalTargetPage
from Logic.planner_page import PlannerPage
from Utils.calorie_target import *
from Utils.users import *
from Logic.weight_goal_page import WeightGoalPage
from Utils.urls import urls


class WeightGoalTest(unittest.TestCase):
    VALID_TARGETS = valid_targets
    INVALID_TARGETS = invalid_target
    USER = get_valid_user('Hosam')

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.get_driver(browser=self.__class__.browser)
        self.browser_wrapper.add_browser_cookie()
        self.browser_wrapper.goto(urls['Weight_Goal'])
        time.sleep(2)

        self.weight_goals_page = WeightGoalPage(self.driver)

    def test_invalid_weight_input_negative(self):
        self.weight_goals_page.update_weight(-1)
        self.assertTrue(self.weight_goals_page.get_validation_message() in['Value must be greater than or equal to 0.','Please select a value that is no less than 0.'])

    def test_invalid_weight_input_greater_than_upper_limit(self):
        self.weight_goals_page.update_weight(1000)
        self.assertTrue(self.weight_goals_page.get_validation_message() in['Value must be less than or equal to 999.','Please select a value that is no more than 999.'])

    def test_valid_weight_input(self):
        weight = 80
        self.weight_goals_page.update_weight(weight)
        self.assertIn(str(weight),self.weight_goals_page.get_last_updated_label())
        weight= 100
        self.weight_goals_page.update_weight(weight)
        self.assertIn(str(weight),self.weight_goals_page.get_last_updated_label())



    def tearDown(self):
        self.browser_wrapper.close_browser()
