# test_runner.py
import json

from login_page_test import LoginPageTest
from planner_page_edit_day_test import MealEditTest
from search_food_popup_test import FoodSearchPopupTest
from tests.ui_tests.test_runner import get_filename
from weight_goal_test import WeightGoalTest
from nutritional_target_input_values_test import *  # Import the tests case
from target_creation_test import  CreateNutritionalTargetsTest
from Utils.json_reader import get_config_data
test_cases = [CreateNutritionalTargetsTest, LoginPageTest, MealEditTest, FoodSearchPopupTest, WeightGoalTest,
              NutritionalTargetsValuesTest]
serial_cases = []


def run_tests_for_browser(browser):
    LoginPageTest.browser = browser
    test_suite = unittest.TestLoader().loadTestsFromTestCase(LoginPageTest)
    unittest.TextTestRunner().run(test_suite)


if __name__ == "__main__":
    config = get_config_data()
    is_parallel = config["parallel"]
    is_serial = config["serial"]
    browsers = config["browser_types"]

    browser = config["browser"]

    run_tests_for_browser(browser)
