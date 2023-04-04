# TODO Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
#  словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
#  имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
#  пустая строка)


users = {'1': {'First_name': 'Max',
               'Last_name': 'Ivanov',
               'Tel': 12345678,
               'Email': 'mi@mail.ru'},
         '2': {'First_name': 'Ivan',
               'Last_name': 'Petrov',
               'Tel': 98745612,
               'Email': ''},
         '3': {'First_name': 'Piotr',
               'Last_name': 'Sidorov',
               'Tel': 98745612}
         }


def users_check(users_dict: dict, key='Email'):
    for key in users_dict.keys():
        # for key1, value1 in value.items():
            #print(f'{value["First_name"]} {value["Last_name"]}')
            print(users_dict.items())



print(users_check(users))
