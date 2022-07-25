# Escreva um programa que leia um número n inteiro 
# qualquer e mostre na tela os n primeiros elementos 
# de uma sequencia de fibonacci


print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
number = int(input('Quantos termos você quer mostrar?: '))
resto = 0
termo1 = 0
termo2 = 1
cont = 3

print('{} - > {}'.format(termo1, termo2), end= ' ')
while cont <= number:
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    print(' -> {}'.format(termo3), end= ' ')
    cont += 1
print('-> FIM')






