# TODO Дан список чисел, необходимо для каждого элемента посчитать сумму его
#  соседей, для крайних чисел одним из соседей является число с противоположной
#  стороны списка

def sum_numbers(lst):
 res = []
 for i in range(len(lst)):
        if i == 0:
            res.append(lst[i] + lst[-1])
        elif i == len(lst) - 1:
            res.append(lst[i-1] + lst[0])
        else:
            res.append(lst[i-1] + lst[i+1])
 return res


numbers = [35, 48, 36, 89, 101, 107, 56, 2, 4, 8, 78, 45, 77]

print(sum_numbers(numbers))
