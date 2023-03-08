# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число
number_1 = float(input('Input number_1: '))
number_2 = float(input('Input number_2: '))
math_operation = input('Input math operation: ')
if math_operation == '+':
    print(f'result: {number_1 + number_2}')
elif math_operation == '-':
    print(f'result: {number_1 - number_2}')
elif math_operation == '/':
    print(f'result: {number_1 / number_2}')
elif math_operation == '*':
    print(f'result: {number_1 * number_2}')
else:
    print('Something wrong!')