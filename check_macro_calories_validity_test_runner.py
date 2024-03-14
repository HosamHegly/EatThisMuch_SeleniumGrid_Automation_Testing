# test_runner.py
import json

from tests.ui_tests.login_page_test import LoginPageTest
from tests.ui_tests.planner_page_edit_day_test import MealEditTest
from tests.ui_tests.search_food_popup_test import FoodSearchPopupTest
from test_runner import get_filename
from tests.ui_tests.weight_goal_test import WeightGoalTest
from tests.ui_tests.nutritional_target_input_values_test import *  # Import the tests case
from tests.ui_tests.target_creation_test import  CreateNutritionalTargetsTest

test_cases = [CreateNutritionalTargetsTest, LoginPageTest, MealEditTest, FoodSearchPopupTest, WeightGoalTest,
              NutritionalTargetsValuesTest]
serial_cases = []


def run_tests_for_browser(browser):
    NutritionalTargetsValuesTest.browser = browser
    test_suite = unittest.TestLoader().loadTestsFromTestCase(NutritionalTargetsValuesTest)
    unittest.TextTestRunner().run(test_suite)


if __name__ == "__main__":
    filename = get_filename("../config.json")
    with open(filename, 'r') as file:
        config = json.load(file)
    is_parallel = config["parallel"]
    is_serial = config["serial"]
    browsers = config["browser_types"]

    browser = config["browser"]

    run_tests_for_browser(browser)
