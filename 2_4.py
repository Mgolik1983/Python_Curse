# number = int(input('Input number: '))
list_n = [2, 3, 5, 7, 89, 4, 9, 7, 6, 54, 87, 69, 32, 33, 22, 34, 56, 38]
n = int(input('Input n: '))
m = int(input('Input m: '))
k = int(input('Input k: '))
# print (n)
# print(m)
count = 0
for i in list_n:
    if list_n[i] % m == 0 and list_n[i] > k:
        print(list_n[i])
    # list_n[i] += 1