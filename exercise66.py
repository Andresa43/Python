# crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
# o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram 
# digitados e qual foi a soma entre eles (desconsiderando o flag)



numbers = cont = soma = 0
while True:
    numbers = int(input('Digite um valor (999 para parar): '))
    if numbers == 999:
        break
    cont += 1
    soma = numbers + soma
print('A soma dos {} valores foi {}!'.format(cont, soma))

