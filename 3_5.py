#Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

def reverse_lst(lst):
    lst = [lst[-i] for i in range(1, len(lst) + 1)]
    return(lst)

numbers = [1, 2, 3, 4, 5, 6, 7]
print(reverse_lst(numbers))

