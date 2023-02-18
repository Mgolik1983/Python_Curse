# Способ 1
sentence = input('Введите предложение: ')
print(sentence.replace(' ', '-'))

# Способ 2
sentence = input('Введите предложение: ')
print('-'.join(sentence.split()))
