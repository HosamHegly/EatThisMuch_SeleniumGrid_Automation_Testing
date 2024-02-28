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
from Utils.food import search_food_names
from Utils.users import *


class MealEditTest(unittest.TestCase):
    Food_Names = search_food_names
    USER = get_valid_user('Hosam')

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.get_driver(browser=self.__class__.browser)
        self.login_page = LoginPage(self.driver)
        self.login_page.login_with_email_password(self.USER['email'], self.USER['password'])
        self.planner_page = PlannerPage(self.driver)

    def test_add_food_to_breakfast_based_on_cals(self):
        for food in self.Food_Names:
            self.planner_page.click_add_food_to_meal_button('Breakfast')
            before_total_cals = int(self.planner_page.get_total_calories())
            self.food_search_popup = FoodSearchPopup(self.driver)
            self.food_search_popup.fill_search_field(food)
            self.food_search_popup.click_search_result_button_by_index(1)
            food_calories = int(self.food_search_popup.get_current_food_calories())
            self.food_search_popup.add_current_food_to_meal()
            after_total_cals = int(self.planner_page.get_total_calories())
            self.assertAlmostEqual(after_total_cals, before_total_cals + food_calories,
                                   msg="Food calories hasn't beend added to total cals correctly", delta=5)

    def tearDown(self):
        self.planner_page.regenerate_meal_plan()
