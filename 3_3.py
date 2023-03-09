# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]
def shift_numbers(lst, n):
    if n < 0:
        n = abs(n)
        for i in range(n):
            lst.append(lst.pop(0))
        else:
            lst.insert(0, lst.pop())


numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers)

shift_numbers(numbers, -2)
print(numbers)

shift_numbers(numbers, 3)
print(numbers)
