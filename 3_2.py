# def morse_coding(word):
word = input('Ввведите слово:')
print(word)
morze_word = []
morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
             'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
              'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.', '0': '-----'}

for i in word.split():
    morze_word = []
    for i in word:
        morze_word.append(morze_dict[i])
   result.append(' '.join(morze_word))
# return morze_word
print(morze_word)
## print(morse_coding(123))

## print('\n'.join(result))