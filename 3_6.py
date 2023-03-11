# TODO Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
#  четные, потом нечётные.

def sort_even_odd(lst):
    for i in lst:
        lst.sort(key=lambda x: x % 2 == 0, reverse=True)
    return lst


numbers = [35, 48, 36, 89, 101, 107, 56, 2, 4, 8, 78, 45, 77]
print(sort_even_odd(numbers))
