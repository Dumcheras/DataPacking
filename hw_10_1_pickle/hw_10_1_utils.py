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

    def del_for_key(self, country_name):
        self.country_name = country_name
        if self.country_name in country_dict:
            del self.country_dict[country_name]
            country_in_dict = ', '.join(country_dict)
            print(f'Упс... страны {country_name} на карте нет... теперь нет.\nОстались {country_in_dict}')
            return self.country_dict
        else:
            country_to_del = self.country_dict.keys()
            str_country = ', '.join(country_to_del)
            print(f'Такой страны нет. Есть вот такие: {str_country}')
            return self.country_dict
