import unittest
import logging
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate

from infra.api_infra.api_wrapper import APIWrapper
from logic.api_logic.get_info import CardsInfo
from utils.json_reader import get_json
from utils.logging_setup import setup_logging


class CardInfoTest(unittest.TestCase):
    test_data_path = 'test_data\\api_test_data\\expected_info.json'
    test_data_schema_path = 'test_data\\api_test_data\\expected_info_schema.json'

    @classmethod
    def setUpClass(cls) -> None:
        setup_logging()
        cls.logger = logging.getLogger("cardInfoTest")
        cls.my_api = APIWrapper()
        cls.card_info = CardsInfo(cls.my_api)
        cls.card_info_response = cls.card_info.get_info()
        cls.card_info_response_json = cls.card_info_response.json()

    def setUp(self):
        self.test_name = self.id().split('.')[-1]

    def test_info_endpoint_status_code(self):
        status_code = self.card_info_response.status_code

        try:
            self.assertEqual(status_code, 200, "didn't receive ok 200 on get request")
            self.logger.info(f"{self.test_name}: Successfully received status code 200 for info endpoint.")
        except AssertionError as e:
            self.logger.error(f"{self.test_name}: Expected status code 200, but received {status_code}. Error: {e}")
            raise

    def test_info_endpoint_schema(self):
        schema = get_json(self.test_data_schema_path)
        try:
            validate(instance=self.card_info_response_json, schema=schema)
            self.logger.info(f"{self.test_name} JSON data successfully validated against the schema.")
        except ValidationError as e:
            self.logger.error(f"{self.test_name} :JSON data did not validate against the schema: {e}")
            self.fail(f"JSON data did not validate against the schema: {e}")

    def test_info_endpoint_response_body(self):
        expected_info = get_json(self.test_data_path)
        test_name = self.id().split('.')[-1]

        for category in expected_info:
            try:
                self.assertEqual(self.card_info_response_json[category], expected_info[category],
                                 f"{category} didn't match expected info")
                self.logger.info(f"{test_name}: {category} matched expected info.")
            except AssertionError as e:
                self.logger.error(f"{test_name}: {category} didn't match expected info. Error: {e}")
                raise
