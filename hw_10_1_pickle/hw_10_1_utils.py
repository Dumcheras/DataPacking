import pickle

'''Основной словарь для ввода и обработки данных\\The main dictionary for data entry and processing'''
country_dict = {}

'''Класс, предназначенный для работы со словарем с помощью вложенных методов\\
\\A class designed to work with a dictionary using nested methods'''


class CountryState:
    def __init__(self, country_dict: dict):
        self.country_dict = country_dict

    '''Метод заполения словаря. Принимает пару ключ|значение при каждом вызове, 
    возвращает заполненный словарь. Ограничение на три записи.\\
    \\The method of filling in the dictionary. Accepts a key|value pair on each call,
    returns a filled dictionary. The limit is three entries.'''

    def add_key_value(self, country_name, country_capital):
        self.country_name = country_name
        self.country_capital = country_capital
        while len(country_dict) < 3:
            self.country_dict[country_name] = country_capital
            return self.country_dict
        return 'словарь полон'

    '''Метод удаляет пару ключ|значение по введенному при вызове ключу\\
    \\The method deletes the key|value pair based on the key entered during the call'''

    def del_for_key(self, country_name):
        self.country_name = country_name
        if self.country_name in country_dict:
            del self.country_dict[country_name]
            country_in_dict = ', '.join(country_dict)
            print(f'Упс... страны {country_name} на карте нет... теперь нет.\nОстались {country_in_dict}\n')
            return self.country_dict
        else:
            country_to_del = self.country_dict.keys()
            str_country = ', '.join(country_to_del)
            print(f'Такой страны нет. Есть вот такие: {str_country}\n')
            return self.country_dict

    '''Метод ищет в словаре значение по ключу\\The method searches the dictionary for the value by key'''

    def get_for_name(self, country_name):
        self.country_name = country_name
        try:
            country_to_search = country_dict[input("Столицу какой страны вы ищете? ")]
            if country_to_search in country_dict.values():
                print(f"Столица {country_to_search}\n")
                return country_to_search
        except KeyError:
            print('Такой страны нет в списке целей\n')

    '''Метод ищет в словаре ключ по значению\\The method searches the dictionary for the key by value'''

    def get_for_capital(self, country_capital):
        self.country_capital = country_capital
        capital_of_country = [key for key, value in self.country_dict.items() if value == self.country_capital]
        str_capital = ', '.join(capital_of_country)
        print(f'Это столица страны {str_capital}\n')
        return capital_of_country

    '''Метод редактирует значение по ключу через перезапись\\The method edits the value by key through overwriting'''

    def replace_capital(self, country_name):
        self.country_name = country_name
        country_name = input("В какой стране меняем столицу? ")
        del self.country_dict[country_name]
        country_capital = input('Введите название новой столицы ')
        self.country_dict[country_name] = country_capital

    '''Метод упаковки словаря при помощи pickle\\The method of packing a dictionary using pickle'''

    @staticmethod
    def pickle_to_file(pickled_dict, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(pickled_dict, file, protocol=4)
            print("Файл упакован")


    '''Метод распаковки словаря при помощи pickle\\The method of unpacking a dictionary using pickle'''

    @staticmethod
    def unpickled_file(pickled_file_name):
        with open(pickled_file_name, 'rb') as file:
            unpickle_data = pickle.load(file)
        return unpickle_data
