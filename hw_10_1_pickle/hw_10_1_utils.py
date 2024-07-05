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

    def get_for_name(self, country_name):
        self.country_name = country_name
        try:
            country_to_search = country_dict[input("Столицу какой страны вы ищете? ")]
            if country_to_search in country_dict.values():
                print(f"Столица {country_to_search}\n")
                return country_to_search
        except KeyError:
            print('Такой страны нет в списке целей\n')

    def get_for_capital(self, country_capital):
        self.country_capital = country_capital
        capital_of_country = [key for key, value in self.country_dict.items() if value == self.country_capital]
        str_capital = ', '.join(capital_of_country)
        print(f'Это столица страны {str_capital}')
        return capital_of_country

    def replace_capital(self, country_name):
        self.country_name = country_name
        country_name = input("В какой стране меняем столицу? ")
        del self.country_dict[country_name]
        country_capital = input('Введите название новой столицы ')
        self.country_dict[country_name] = country_capital

    @staticmethod
    def pickle_to_file(pickled_dict, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(pickled_dict, file, protocol=4)
        return "Файл упакован"
    @staticmethod
    def unpickled_file(pickled_file_name):
        with open(pickled_file_name, 'rb') as file:
            unpickle_data = pickle.load(file)
        return unpickle_data