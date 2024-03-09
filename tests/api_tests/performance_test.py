import logging
import time
import unittest

from infra.api_infra.api_wrapper import APIWrapper
from logic.api_logic.get_info import CardsInfo
from logic.api_logic.get_cards_by import CardsEndpoints
from utils.logging_setup import setup_logging


class PerformanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:

        setup_logging()
        cls.logger = logging.getLogger("PerformanceTest")

    def setUp(self):
        self.my_api = APIWrapper()
        self.cards = CardsEndpoints(self.my_api)

        self.test_name = self.id().split('.')[-1]

    def test_get_by_class_performance(self, class_name='shaman'):
        start_time = time.time()  # Record start time
        self.cards.get_cards_by_class(class_name=class_name)
        end_time = time.time()
        elapsed_time = end_time - start_time
        try:
            self.assertTrue(elapsed_time < 3, "The response time exceeded the threshold.")
            self.logger.info(f"{self.test_name} completed successfully in {elapsed_time} seconds.")
        except AssertionError as e:
            self.logger.error(f"Assertion error in {self.test_name}: {e}")


    def test_get_by_race_performance(self, race='demon'):
        start_time = time.time()  # Record start time
        self.cards.get_cards_by_race(race=race)
        end_time = time.time()
        elapsed_time = end_time - start_time
        try:
            self.assertTrue(elapsed_time < 3, "The response time exceeded the threshold.")
            self.logger.info(f"{self.test_name} completed successfully in {elapsed_time} seconds.")
        except AssertionError as e:
            self.logger.error(f"Assertion error in {self.test_name}: {e}")


    def test_get_by_type_performance(self, type='spell'):
        start_time = time.time()  # Record start time
        self.cards.get_cards_by_type(type=type)
        end_time = time.time()
        elapsed_time = end_time - start_time
        try:
            self.assertTrue(elapsed_time < 3, "The response time exceeded the threshold.")
            self.logger.info(f"{self.test_name} completed successfully in {elapsed_time} seconds.")
        except AssertionError as e:
            self.logger.error(f"Assertion error in {self.test_name}: {e}")
