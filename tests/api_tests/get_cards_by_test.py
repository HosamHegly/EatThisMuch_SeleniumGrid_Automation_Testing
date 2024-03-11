import os
import unittest
import logging
from parameterized import parameterized
from infra.api_infra.api_wrapper import APIWrapper
from logic.api_logic.get_cards_by import CardsEndpoints
from logic.api_logic.get_info import CardsInfo
from Utils.json_reader import get_json
from Utils.logging_setup import setup_logging

params_file_path = os.path.join('test_data', 'api_test_data','params_filter.json')
info_file_path = os.path.join('test_data', 'api_test_data', 'expected_info.json')


class CardFilterTest(unittest.TestCase):

    def setUp(self):
        self.my_api = APIWrapper()
        self.card_info = CardsEndpoints(self.my_api)
        self.test_name = self.id().split('.')[-1]

    @parameterized.expand(get_json(info_file_path)['classes'])
    def test_by_class_without_params(self, class_name):
        card_response = self.card_info.get_cards_by_class(class_name)
        response_body = card_response.json()
        for card in response_body:
            card_class = card.get('playerClass')
            self.assertEqual(class_name, card_class,
                             f'Received card class does not match requested class name parameter {class_name}.')

    @parameterized.expand(get_json(params_file_path)['by_class'])
    def test_by_class_endpoint_response_body_with_valid_params(self, class_name, body):
        card_class_response = self.card_info.get_cards_by_class(class_name=class_name, body=body)
        response_body = card_class_response.json()

        for expected_param_key, expected_param_value in body.items():
            for card in response_body:
                actual_value = card.get(expected_param_key)
                self.assertEqual(actual_value, expected_param_value,
                                 f"Expected {expected_param_key} to be {expected_param_value}, got {actual_value} in one of the cards.")

    def test_by_class_endpoint_response_body_with_invalid_params(self, class_param='invalid'):
        card_response = self.card_info.get_cards_by_class(class_name=class_param, body={'attack':'invalid','health':'invalid'})
        self.assertEqual(404, card_response.status_code, 'API did not return HTTP 404 Bad Request for invalid parameters. Error')

    @parameterized.expand(get_json(info_file_path)['races'])
    def test_by_race_without_params(self, race):
        card_response_race = self.card_info.get_cards_by_race(race)
        response_body = card_response_race.json()
        for card in response_body:
            card_class = card.get('race')
            self.assertEqual(race, card_class,
                             f'Received card race does not match requested class name parameter {race} and body {response_body}')

    @parameterized.expand(get_json(params_file_path)['by_race'])
    def test_by_race_endpoint_response_body_with_valid_params(self, race, body):
        card_response = self.card_info.get_cards_by_race(race=race, body=body)
        status_code = card_response.status_code
        response_body = card_response.json()
        for expected_param_key, expected_param_value in body.items():
            for card in response_body:
                actual_value = card.get(expected_param_key)
                self.assertEqual(actual_value, expected_param_value,
                                 f"Expected {expected_param_key} to be {expected_param_value}, got {actual_value} in one of the cards.")

    def test_by_race_endpoint_response_body_with_invalid_params(self, race='invalid'):
        card_response = self.card_info.get_cards_by_race(race=race, body={'attack': 'invalid', 'health': 'invalid'})

        self.assertEqual(404, card_response.status_code, 'API did not return HTTP 404 Bad Request for invalid parameters. Error')
