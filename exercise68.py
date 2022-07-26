# faça um programa que jogue par ou impar com o computador. 
# o jogo só será interrompido quando o jogador PERDER, mostrando
# o total de vitórias consecutivas que ele conquistou no final.

from time import sleep
import random

computador = random.randint(0, 10)
cont = 0
while True:
    valor = int(input('Digite um valor: '))       
    par_impar = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print('-'*40)
    soma = valor + computador
    if par_impar == 'P' and soma%2!=0:
        par_impar = 'ÍMPAR'
        break
    if par_impar == 'I' and soma%2==0:
        par_impar = 'PAR'
        break
    if par_impar == 'P' and soma%2==0:
        print('Você jogou {} e o computador {}. Total de {} DEU PAR'.format(valor, computador, soma))
        print('Você VENCEU!')
        print('-'*40)
        print('Vamos jogar novamente...')
        cont+=1
    elif par_impar == 'I' and soma%2!=0:
        print('Você jogou {} e o computador {}. Total de {} DEU ÍMPAR'.format(valor, computador, soma))
        print('Você VENCEU!')
        print('-'*40)
        print('Vamos jogar novamente...')
        cont+=1
print('Você jogou {} e o computador {}. Total de {} deu {}'.format(valor, computador, soma, par_impar))
print('-'*40)
print('Você PERDEU!')
print('=-'*20)
print('GAME OVER! Você venceu {} vezes'.format(cont))
  

