import unittest
import logging
from parameterized import parameterized
from infra.api_infra.api_wrapper import APIWrapper
from logic.api_logic.get_cards_by import CardsEndpoints
from logic.api_logic.get_info import CardsInfo
from utils.json_reader import get_json
from utils.logging_setup import setup_logging
params_file_path = "test_data\\api_test_data\\params_filter.json"
info_file_path = "test_data\\api_test_data\\expected_info.json"


class CardFilterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        setup_logging()
        cls.logger = logging.getLogger('CardFilterTestClass')

    def setUp(self):
        self.my_api = APIWrapper()
        self.card_info = CardsEndpoints(self.my_api)
        self.test_name = self.id().split('.')[-1]

    @parameterized.expand(get_json(info_file_path)['classes'])
    def test_by_class_without_params(self, class_name):
        card_response = self.card_info.get_cards_by_class(class_name)
        status_code = card_response.status_code
        response_body = card_response.json()
        try:
            self.assertEqual(status_code, 200)
            self.logger.info(f"{self.test_name}: Successfully received status code 200 for info endpoint.")
        except AssertionError as e:
            self.logger.error(f"{self.test_name}: Expected status code 200, but received {status_code}. Error: {e}")
            return

        for card in response_body:
            try:
                card_class = card.get('playerClass')
                self.assertEqual(class_name, card_class)
                self.logger.info(
                    f"{self.test_name}: Received card class matches the requested class name parameter {class_name}.")
            except AssertionError as e:
                self.logger.error(
                    f"{self.test_name}: Received card class does not match requested class name parameter {class_name}. Error: {e}")
                break  # Exit the loop after the first failure

    @parameterized.expand(get_json(params_file_path)['by_class'])
    def test_by_class_endpoint_response_body_with_valid_params(self, class_name, body):
        card_response = self.card_info.get_cards_by_class(class_name=class_name, body=body)
        status_code = card_response.status_code
        response_body = card_response.json()

        try:
            self.assertEqual(status_code, 200)
            self.logger.info(
                f"{self.test_name}: Successfully received status code 200 for by class {class_name} endpoint and body {body} .")
        except AssertionError as e:
            self.logger.error(
                f"{self.test_name}: Expected status code 200, but received {status_code} in get by class {class_name} with body {response_body}. Error: {e}")
            return
        for expected_param_key, expected_param_value in body.items():
            for card in response_body:
                actual_value = card.get(expected_param_key)
                self.assertEqual(actual_value, expected_param_value,
                                 f"Expected {expected_param_key} to be {expected_param_value}, got {actual_value} in one of the cards.")
                self.logger.info(
                    f"{self.test_name}: {expected_param_key} correctly matched {expected_param_value} in card.")

    def test_by_class_endpoint_response_body_with_invalid_params(self,class_name='mage'):
            card_response = self.card_info.get_cards_by_class(class_name=class_name, body={'attack': 'invalid', 'health': 'invalid'})
            status_code = card_response.status_code
            try:
                self.assertEqual(404, status_code)
                self.logger.info(
                    f"{self.test_name}: Successfully returned 404 for bad request parameters.")
            except AssertionError as e:
                self.logger.error(
                    f"{self.test_name}: API did not return HTTP 404 Bad Request for invalid parameters. Error: {e}")

    @parameterized.expand(get_json(info_file_path)['races'])
    def test_by_race_without_params(self, race):
        card_response = self.card_info.get_cards_by_race(race)
        status_code = card_response.status_code
        response_body = card_response.json()
        try:
            self.assertEqual(200,status_code)
            self.logger.info(f"{self.test_name}: Successfully received status code 200 for info endpoint.")
        except AssertionError as e:
            self.logger.error(f"{self.test_name}: Expected status code 200, but received {status_code}. Error: {e}")
            return

        for card in response_body:
            try:
                card_class = card.get('race')
                self.assertEqual(race, card_class)
                self.logger.info(
                    f"{self.test_name}: Received card race matches the requested class name parameter {race}.")
            except AssertionError as e:
                self.logger.error(
                    f"{self.test_name}: Received card race does not match requested class name parameter {race}. Error: {e}")
                break

    @parameterized.expand(get_json(params_file_path)['by_race'])
    def test_by_race_endpoint_response_body_with_valid_params(self, race, body):
        card_response = self.card_info.get_cards_by_race(race=race, body=body)
        status_code = card_response.status_code
        response_body = card_response.json()
        try:
            self.assertEqual(200,status_code)
            self.logger.info(
                f"{self.test_name}: Successfully received status code 200 for by race {race} endpoint and body {body} .")
        except AssertionError as e:
            self.logger.error(
                f"{self.test_name}: Expected status code 200, but received {status_code} in get by race {race} with body {response_body}. Error: {e}")
            return
        for expected_param_key, expected_param_value in body.items():
            for card in response_body:
                actual_value = card.get(expected_param_key)
                self.assertEqual(actual_value, expected_param_value,
                                 f"Expected {expected_param_key} to be {expected_param_value}, got {actual_value} in one of the cards.")
                self.logger.info(
                    f"{self.test_name}: {expected_param_key} correctly matched {expected_param_value} in card.")

    def test_by_race_endpoint_response_body_with_invalid_params(self,race='demon'):
        card_response = self.card_info.get_cards_by_race(race=race, body={'attack':'invalid','health':'invalid'})
        status_code = card_response.status_code
        try:
            self.assertEqual(404,status_code)
            self.logger.info(
                f"{self.test_name}: Successfully returned 404 for bad request parameters.")
        except AssertionError as e:
            self.logger.error(
                f"{self.test_name}: API did not return HTTP 404 Bad Request for invalid parameters. Error: {e}")

