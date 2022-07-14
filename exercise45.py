import random
itens = ('Pedra', 'Papel', 'Tesoura')
computer = random.randint(1, 3)
print('''Suas opções:
1 - pedra
2 - papel
3 - tesoura''')
choices = int(input('Qual é a sua jogada? '))
print('Computador escolheu {} '.format(itens[computer-1]))
print('Jogador escolheu {}'.format(itens[choices-1]))
print('-='*20)

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
