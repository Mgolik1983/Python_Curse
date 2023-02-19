number_one = int(input('Введите первое число: '))
number_two = int(input('Введите второе число: '))
number_three = int(input('Введите третье число: '))
str_numbers = f'{number_one < 0}, {number_two < 0}, {number_three < 0}'
print('Количество положительных чисел: ', str_numbers.count('True'))
print('Количество положительных чисел: ', str_numbers.count('False'))
