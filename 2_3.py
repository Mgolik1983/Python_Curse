# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры
# [1: ['name': None, 'email': None], ]
import collections
data1 {
    'a': 1,
    'b': 2
}
data2 {
    'c': 3,
    'd': 4
  }
chain = collections.ChainMap (data1,data2)
print(chain)