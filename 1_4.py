number_one = int(input('Введите первое число: '))
number_two = int(input('Введите второе число: '))
number_three = int(input('Введите третье число: '))
count_positive_numbers = 0
count_negative_numbers = 0
if number_one > 0:
    count_positive_numbers += 1
else:
    count_negative_numbers += 1
if number_two > 0:
    count_positive_numbers += 1
else:
    count_negative_numbers += 1
if number_three > 0:
    count_positive_numbers += 1
else:
    count_negative_numbers += 1
print(f'Количество положительных чисел: {count_positive_numbers}, ',
      f'количество отрицательных чисел: {count_negative_numbers}')
