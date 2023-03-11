# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные
def sort_even_odd(lst):
    for i in lst:
        lst.sort(key=lambda x: x % 2 == 0, reverse=True)
    return lst

numbers = [12, 13, 4, 7, 18, 21, 9, 56, 8, 9, 17, 29, 34]
print(sort_even_odd(numbers))
