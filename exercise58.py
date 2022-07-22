# Melhore o jogo do DESAFIO029 onde o computador vai "pensar" em um número 
# entre 0 e 10. Só que agora vai tentar advinhar até acertar, mostrando no 
# final quantos palpites foram necessários para vencer


import random
from time import sleep

conguess = 0
numbers = random.randint(0, 10)
number_choice = int(input('Qual foi o número escolhido pelo computador de 0 a 10? '))

while number_choice != numbers:
    conguess += 1
    sleep(1)
    if number_choice < numbers:
        print('Mais... Tente mais uma vez.')
    elif number_choice > numbers:
        print('Menos... Tente mais uma vez.')
    number_choice = int(input('Qual é o eu palpite? '))
print('Você escolheu o número {} que é igual ao número {} escolhido pelo computador'.format(number_choice, numbers))
print('Você precisou de {} palpites para vencer'.format(conguess))


