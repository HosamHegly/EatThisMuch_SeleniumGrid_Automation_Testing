from Utils.json_reader import get_config_data


class CardsEndpoints:

    def __init__(self, api_object):
        self.my_api = api_object
        self.url = get_config_data()['api_url'] + '/cards'
        self.config = get_config_data()
        self.headers = self.config["api_headers"]

    def get_cards_by_class(self, class_name, body=None):
        return self.my_api.api_get_request(f"{self.url}/classes/{class_name}", body=body,header=self.headers)

    def get_cards_by_race(self, race, body=None):
        return self.my_api.api_get_request(f"{self.url}/races/{race}", body=body,header=self.headers)

    def get_cards_by_set(self, set_name, body=None):  # Fixed parameter name from 'class_name' to 'set_name'
        return self.my_api.api_get_request(f"{self.url}/sets/{set_name}", body=body,header=self.headers)

    def get_cards_by_quality(self, quality, body=None):
        return self.my_api.api_get_request(f"{self.url}/qualities/{quality}", body=body,header=self.headers)

    def get_cards_by_faction(self, faction, body=None):
        return self.my_api.api_get_request(f"{self.url}/factions/{faction}", body=body,header=self.headers)

    def get_cards_by_type(self, type, body=None):
        return self.my_api.api_get_request(f"{self.url}/types/{type}", body=body,header=self.headers)
