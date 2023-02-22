# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры
# {1: {'name': None,
#      'email': None} }
import  collections
n =int(input('n: '))
list_n = [1 + n for n in range(n)]
users_n = dict.fromkeys(list_n)
# for i in range(users_n)
   
print(list_n)
print(users_n)

