# Вывести первые N цисел кратные M и больше K
numbers = [2, 3, 5, 7, 89, 4, 9, 7, 6, 54, 87, 69, 32, 33, 22, 34, 56, 38]
counter = 0
n = int(input('Input n: '))
m = int(input('Input m: '))
k = int(input('Input k: '))
for number in numbers:
    if number % m == 0 and number > k and counter < n:
        counter += 1
        print(number)
