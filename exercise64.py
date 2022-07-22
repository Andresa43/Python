
# Crie um programa que leia vários números inteiros 
# pelo teclado. O programa só vai parar quando o usuário 
# digitar o valor 999, que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a soma entre 
# eles (desconsiderando o flag)


cont = -1
numbers = 0
save = 0
while numbers != 999:
    numbers = int(input('Digite um número inteiro ou \033[31m999\033[m para encerrar o programa: '))
    save = (save + numbers)
    cont+=1   
print('Foram digitados {} números e a soma entre eles é {}'.format(cont, save-999))

