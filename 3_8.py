# TODO Дан словарь, ключ - Название страны, значение - список городов, на вход
#  поступает город, необходимо сказать из какой он страны

def find_country():
 city = input('Input a city: ').title()
 Countries = {'Belarus': ['Minsk', 'Brest', 'Vitebsk', 'Gomel', 'Grodno', 'Mogilev'],
              'Russia': ['Moscow', 'Sochi', 'Saint Petersburg', 'Novosibirsk', 'Volgograd'],
              'USA': ['New York', 'Los Angeles', 'Chicago', 'Washington']}
 for name, contents in Countries.items():
     if city in contents:
         print(f'Your country is: {name}')

find_country()
