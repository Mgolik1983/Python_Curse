def convert_to_bin(number_dec):
    number_bin = ''
    while number_dec > 0:
        number_bin = str(number_dec % 2) + number_bin
        number_dec = number_dec // 2
    return number_bin

print(convert_to_bin(input()))
