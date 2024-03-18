import time
import unittest

from infra.api_infra.api_wrapper import APIWrapper
from infra.jira_wrapper import JiraClient
from logic.api_logic.get_cards_by import CardsEndpoints


class PerformanceTest(unittest.TestCase):

    def setUp(self):
        self.my_api = APIWrapper()
        self.cards = CardsEndpoints(self.my_api)
        self.jira_client = JiraClient()
        self.test_name = self.id().split('.')[-1]
        self.test_failed = False

    def tearDown(self):
        if self.test_failed:
            summary = f"Test failed: {self.test_name}"
            description = self.error_msg
            project_key = "NEW"
            self.jira_client.create_issue(summary, description, project_key)

    def test_get_by_class_performance(self, class_name='shaman'):
        try:
            start_time = time.time()
            self.cards.get_cards_by_class(class_name=class_name)
            end_time = time.time()
            self.assertTrue(end_time - start_time < 3, "The response time exceeded the threshold.")
        except AssertionError as e:
            self.test_failed = True
            self.error_msg = str(e)
            raise

    def test_get_by_race_performance(self, race='demon'):
        try:
            start_time = time.time()
            self.cards.get_cards_by_race(race=race)
            end_time = time.time()
            self.assertTrue(end_time - start_time < 3, "The response time exceeded the threshold.")
        except AssertionError as e:
            self.test_failed = True
            self.error_msg = str(e)
            raise

    def test_get_by_type_performance(self, type='spell'):
        try:
            start_time = time.time()
            self.cards.get_cards_by_type(type=type)
            end_time = time.time()
            self.assertTrue(end_time - start_time < 3, "The response time exceeded the threshold.")
        except AssertionError as e:
            self.test_failed = True
            self.error_msg = str(e)
            raise
