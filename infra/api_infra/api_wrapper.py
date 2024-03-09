import requests
import logging
from utils.json_reader import get_config_data
from utils.logging_setup import setup_logging


class APIWrapper:

    def __init__(self):
        self.response = None
        self.my_request = requests
        self.config = get_config_data()
        self.headers = self.config["api_headers"]
        setup_logging()
        self.logger = logging.getLogger(__name__)

    def api_get_request(self, url, body=None):
        self.logger.info(f"Making GET request to {url} with body: {body}")
        self.response = self.my_request.get(url, params=body, headers=self.headers)
        self.logger.info(f"Received response: {self.response.status_code}")
        return self.response

    def api_post_request(self, url, body=None):
        self.logger.info(f"Making POST request to {url} with body: {body}")
        self.response = self.my_request.post(url, params=body, headers=self.headers)
        self.logger.info(f"Received response: {self.response.status_code}")
        return self.response

    def api_put_request(self, url, body=None):
        self.logger.info(f"Making PUT request to {url} with body: {body}")
        self.response = self.my_request.put(url, params=body, headers=self.headers)
        self.logger.info(f"Received response: {self.response.status_code}")
        return self.response
