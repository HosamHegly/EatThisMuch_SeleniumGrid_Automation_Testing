import unittest

from infra.ui_infra.browser_wrapper import BrowserWrapper
from logic.ui_logic.food_search_popup import FoodSearchPopup
from logic.ui_logic.planner_page import PlannerPage
from test_data.ui_test_data.food import *
from test_data.ui_test_data.users import *
from test_data.ui_test_data.urls import urls

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

    def tearDown(self):
        self.planner_page.regenerate_meal_plan()
