
from hw_10_1_pickle.hw_10_1_utils import country_dict, CountryState




country_of_world = CountryState(country_dict)
country_of_world.add_key_value('Россия', 'Москва')
country_of_world.add_key_value('Англия', 'Лондон')
country_of_world.add_key_value('Германия', 'Берлин')

print(country_dict)

country_of_world.get_for_name(())  # Ввод ключа для поиска осуществляется в методе
country_of_world.del_for_key(input("Введите страну, которую хотите удалить: "))
country_of_world.get_for_capital(input('Введите столицу '))
country_of_world.replace_capital(())  # Ввод ключа для поиска и присвоение значения осуществляется в методе

print(country_dict)

country_of_world.pickle_to_file(country_dict, 'dict_to_pickle.txt')
print(country_of_world.unpickled_file('dict_to_pickle.txt'))
