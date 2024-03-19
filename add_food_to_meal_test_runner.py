# test_runner.py
import json
import unittest

from tests.ui_tests.login_page_test import LoginPageTest

from Utils.json_reader import get_config_data
from tests.ui_tests.planner_page_edit_day_test import MealEditTest

test_cases = [LoginPageTest
              ]
serial_cases = []


def run_tests_for_browser(browser):
    MealEditTest.browser = browser
    test_suite = unittest.TestLoader().loadTestsFromTestCase(MealEditTest)
    unittest.TextTestRunner().run(test_suite)


if __name__ == "__main__":
    config = get_config_data()
    is_parallel = config["parallel"]
    is_serial = config["serial"]
    browsers = config["browser_types"]

    browser = config["browser"]

    run_tests_for_browser(browser)
