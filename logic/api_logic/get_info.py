from utils.json_reader import get_config_data
import json



class CardsInfo:

    def __init__(self, api_object):
        self.my_api = api_object
        self.url = get_config_data()['api_url']

    def get_info(self):
        self.cards_info = self.my_api.api_get_request(f'{self.url}/info')
        return self.cards_info



