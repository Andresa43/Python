import random

nAleatory = random.randint(0, 5)

n = int(input('Qual foi o número escolhido pelo computador? '))

if n == nAleatory: 
    print('O número escolhido foi o {}. Parabéns, você acertou!'.format(nAleatory))

else:
    print('O número escolhido foi o {}. Você errou! Tente de novo na próxima.'.format(nAleatory))