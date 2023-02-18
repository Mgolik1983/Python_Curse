#Пользователь вводит предложение, заменить все пробелы на "-" 2-мя
#способами
# - 1 -
sentence = input('Введите предложение: ')
print(sentence.replace(' ' , '-'))

# - 2 -
sentence = input('Введите предложение: ')
print('-'.join(sentence.split()))
