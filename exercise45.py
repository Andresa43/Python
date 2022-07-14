import random

computer = random.randint(1, 3)
choices = int(input('Qual é a sua jogada? \n 1 - pedra \n 2 - papel \n 3 - tesoura \n Digite o número correspondente:'))
itens = ('Pedra', 'Papel', 'Tesoura')
print('Computador escolheu {} '.format(itens[computer]))
print('Jogador escolheu {} '.format(itens[choices]))

print('-=*'*20)
if choices == 1 and computer == 3:
    print('Você venceu!')
elif choices == 2 and computer == 1:
    print('Você venceu!')
elif choices == 3 and computer == 2:
    print('Você venceu!')
elif choices == computer:
    print('Empate')
else:
    print('Computador vence')
