import time

import unittest

from infra.ui_infra.browser_wrapper import BrowserWrapper
from logic.ui_logic.nutritional_target_page import NutritionalTargetPage
from test_data.ui_test_data.calorie_target import *
from test_data.ui_test_data.users import *
from test_data.ui_test_data.urls import urls


class CreateNutritionalTargetsTest(unittest.TestCase):
    _non_parallel = True
    VALID_TARGETS = valid_targets
    INVALID_TARGETS = invalid_target
    USER = get_valid_user('Hosam')

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.get_driver(browser=self.__class__.browser)

        self.browser_wrapper.add_browser_cookie()
        self.browser_wrapper.goto(urls['Nutritional_Target'])
        time.sleep(2)
        self.nutritional_targets_page = NutritionalTargetPage(self.driver)

    def test_create_valid_nutritional_target(self):
        for target in self.VALID_TARGETS:
            self.nutritional_targets_page.create_nurtional_target(title=target["title"], calories=target["calories"],
                                                                  fiber=target["fiber"], max_fats=target["max_fats"],
                                                                  min_fats=target["min_fats"],
                                                                  min_carbs=target['min_carbs'],
                                                                  max_carbs=target['max_carbs'],
                                                                  max_proteins=target['max_proteins'],
                                                                  min_proteins=target['min_proteins'])
            self.assertIn(target["title"], self.nutritional_targets_page.get_target_titles())


    def tearDown(self):
        self.nutritional_targets_page.delete_last_target()
        self.browser_wrapper.close_browser()
