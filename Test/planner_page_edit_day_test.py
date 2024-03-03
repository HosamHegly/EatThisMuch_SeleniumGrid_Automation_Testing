import time

import selenium
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import unittest
import json

from Infra.browser_wrapper import BrowserWrapper
from Logic.food_search_popup import FoodSearchPopup
from Logic.login_page import LoginPage
from Logic.planner_page import PlannerPage
from Utils.food import *
from Utils.users import *
from Utils import cookies
from Utils.urls import urls

class MealEditTest(unittest.TestCase):
    _non_parallel = True
    Food_Names = valid_search_food_names
    USER = get_valid_user('Hosam')
    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.get_driver(browser=self.__class__.browser)

        self.browser_wrapper.add_browser_cookie()
        self.browser_wrapper.goto(urls['Planner_Page'])


        self.planner_page = PlannerPage(self.driver)

    def test_add_food_to_breakfast(self):
        for food in self.Food_Names:
            self.planner_page.click_add_food_to_meal_button('Breakfast')
            before_total_cals = int(self.planner_page.get_total_calories())
            self.food_search_popup = FoodSearchPopup(self.driver)
            self.food_search_popup.fill_search_field(food)
            food_name=self.food_search_popup.choose_random_food_from_list()
            food_calories = int(self.food_search_popup.get_current_food_calories())
            self.food_search_popup.add_current_food_to_meal()
            after_total_cals = int(self.planner_page.get_total_calories())
            self.assertTrue(food_name in self.planner_page.get_breakfast_list())
            self.assertAlmostEqual(after_total_cals, before_total_cals + food_calories,
                                   msg="Food calories hasn't beend added to total cals correctly", delta=5)
            time.sleep(1)

    def tearDown(self):
        self.planner_page.regenerate_meal_plan()
        time.sleep(2)
