# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры
# {1: {'name': None,'email': None}, }
n = int(input('Введите количество пользователей: '))
users_n = dict.fromkeys([1 + n for n in range(n)], {'name', 'email'})
for i in users_n:
    users_n[i] = {'name': input('Name: '), 'email': input('Email: ')}
print(users_n)
