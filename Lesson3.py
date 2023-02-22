from string import printable
#sms = input('input SMS: ')
def sms_func (sms):
 bytes_count = 0
 for el in sms:
  if el in printable:
   bytes_count += 1
  else:
   bytes_count += 2
   sms_count = bytes_count / 140
   if sms_count.is_integer():
    return int(sms_count)
   else:
    return int(sms_count) + 1
res = sms_func ('fnbnnfbkdfjbnkjbnkjfdnbkfdjbnkfjdbnfjknb  ====f ejgksjn kgnewngew   kklxkfnblfkdnl === == 11111')
print(res)
