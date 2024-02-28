# test_runner.py
import json
import unittest
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from os.path import dirname, join

from Test.login_page_test import LoginPageTest
from Test.planner_page_edit_day_test import MealEditTest
from Test.search_food_popup_test import FoodSearchPopupTest
from Test.weight_goal_test import WeightGoalTest
from nutritional_target_input_values_test import *  # Import the test case
from infra.browser_wrapper import BrowserWrapper
from target_creation_test import CreateTargetTest, CreateNutritionalTargetsTest


def get_filename(filename):
    here = dirname(__file__)
    output = join(here, filename)
    return output


def run_tests_for_browser(browser):
    CreateNutritionalTargetsTest.browser = browser
    test_suite = unittest.TestLoader().loadTestsFromTestCase(CreateNutritionalTargetsTest)
    unittest.TextTestRunner().run(test_suite)


if __name__ == "__main__":
    filename = get_filename("../config.json")
    with open(filename, 'r') as file:
        config = json.load(file)
    is_parallel = config["parallel"]
    is_serial = config["serial"]

    is_grid = config["grid"]
    browsers = config["browser_types"]
    if is_parallel:
        with ThreadPoolExecutor(max_workers=len(browsers)) as executor:
            executor.map(run_tests_for_browser, browsers)
    elif is_serial:
        for browser in browsers:
            run_tests_for_browser(browser)
    else:
        browser = config["browser"]
        run_tests_for_browser(browser)
