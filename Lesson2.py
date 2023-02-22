# a = input('Enter a:')
# while not a.isdigit():
#     a = input('Enter a:')
# print(a)

# a = input('a: ')
# max_num = max(a)
# print(max_num)

# m = [25, 10, 5, 1]
#print(sum(m))
#sum_money = input('Sum: ')
#while



limit_summ = int(input('limit_sum: '))
proc = float(input('proc: '))
target_sum = limit_summ*2
year = 0
while limit_summ < target_sum:
    year += 1
    limit_summ += limit_summ*proc/100
print(year)


bytes_count = 0
     for el in sms:
     if el in printable:
      bytes_count +=1
     else:
      bytes_count +=2
   sms_count = bytes_count / 140
   if sms_count.is_integer():
    return int(sms_count)
   else:
    return int(sms_count) +1