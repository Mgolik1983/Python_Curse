number_one = int(input('Введите первое слагаемое: '))
number_two = int(input('Введите второе слагаемое: '))
number_three = int(input('Введите третье слагаемое: '))
print(round(((number_one+number_two+number_three)/3), 3))
# Способ 2
numbers = (int(input('Введите первое слагаемое: ')),
           int(input('Введите второе слагаемое: ')),
           int(input('Введите третье слагаемое: ')))
print(round(sum(numbers)/len(numbers), 3))
