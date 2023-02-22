# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры
sentence = input('Введите предложение: ')
dict_chars = dict.fromkeys(sentence,0)
for i in sentence:
    dict_chars[i] += 1
print(dict_chars)
