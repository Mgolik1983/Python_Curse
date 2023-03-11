# TODO Дан словарь, ключ - Название страны, значение - список городов, на вход
#  поступает город, необходимо сказать из какой он страны

def find_country():
    countries = {'Belarus': ['Minsk', 'Brest', 'Vitebsk', 'Gomel', 'Grodno', 'Mogilev'],
                 'Russia': ['Moscow', 'Sochi', 'Saint Petersburg', 'Novosibirsk', 'Volgograd'],
                 'USA': ['New York', 'Los Angeles', 'Chicago', 'Washington']}
    city = str(input('Input a city: ').title())
    for name, contents in countries.items():
        if city in contents:
            print(f'Your country is: {name}')
        elif city not in contents:
            break
    print(f'Your country not found')


find_country()
