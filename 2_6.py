# Вывести четные числа от 2 до N по 5 в строку
from itertools import zip_longest
numbers = iter([*range(2, int(input('Input n: ')) + 1, 2)])
numbers = list(zip_longest(numbers, numbers, numbers, numbers, numbers))
print(numbers)
