phrase = str(input('Digite uma frase qualquer: ')).strip().upper()

words = phrase.split()
together = ''.join(words)
# inverse = ''
inverse = together[::-1]

'''for letter in range(len(together) -1, -1, -1):
    inverse += together[letter]'''
print('O inverso de {} é {}'.format(phrase, inverse))

if together == inverse:
    print('Temos um Palíndromo'.format(phrase))
else:
    print('Não é um palíndromo'.format(phrase))


