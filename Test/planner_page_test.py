import concurrent.futures.thread
import time

import selenium
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import unittest
import json

from infra.browser_wrapper import BrowserWrapper
from logic.food_search_popup import FoodSearchPopup
from logic.login_page import LoginPage
from logic.planner_page import PlannerPage
from Utils.helper_functions import *


class PlannerPageTest(unittest.TestCase):

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.get_driver(browser=self.__class__.browser)
        self.login_page = LoginPage(self.driver)
        self.login_page.login_with_email_password('hosam', 'hosam123')
        self.planner_page = PlannerPage(self.driver)

    def test_search_food_feature_in_add_food(self):
        self.planner_page.click_add_food_to_meal_button('Breakfast')
        self.food_search_popup = FoodSearchPopup(self.driver)
        food_name = "apple"
        self.food_search_popup.fill_search_field("apple")

        all_food_results = self.food_search_popup.get_all_results_food_names_and_ingredients()
        for food in all_food_results:
            self.assertTrue(food_name in food['name'] or is_contained_in(food_name,food['ingredients']))

    def tearDown(self):
        self.browser_wrapper.close_browser()
