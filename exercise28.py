import random
from time import sleep

nAleatory = random.randint(0, 5)

n = int(input('Qual foi o número escolhido pelo computador? '))
print('PROCESSANDO...')
sleep(3)

if n == nAleatory: 
    print('O número escolhido foi o {}. Parabéns, você acertou!'.format(nAleatory))

else:
    print('O número escolhido foi o {}. O computador venceu!'.format(nAleatory))

