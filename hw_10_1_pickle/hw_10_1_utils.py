import pickle
country_dict = {}
class CountryState:
    def __init__(self, country_dict: dict):
        self.country_dict = country_dict
    def add_key_value(self, country_name, country_capital):
        self.country_name = country_name
        self.country_capital = country_capital
        while len(country_dict) < 3:
            self.country_dict[country_name] = country_capital
            return self.country_dict
        return 'словарь полон'