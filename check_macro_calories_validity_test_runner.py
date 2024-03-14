# test_runner.py
import json

from Utils.json_reader import get_config_data
from tests.ui_tests.nutritional_target_input_values_test import *  # Import the tests case

test_cases =  [NutritionalTargetsValuesTest]
serial_cases = []


def run_tests_for_browser(browser):
    NutritionalTargetsValuesTest.browser = browser
    test_suite = unittest.TestLoader().loadTestsFromTestCase(NutritionalTargetsValuesTest)
    unittest.TextTestRunner().run(test_suite)


if __name__ == "__main__":
    filename = get_config_data()
    with open(filename, 'r') as file:
        config = json.load(file)
    is_parallel = config["parallel"]
    is_serial = config["serial"]
    browsers = config["browser_types"]

    browser = config["browser"]

    run_tests_for_browser(browser)
