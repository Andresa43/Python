# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar.
# No final, mostre:

# a) quantas pessoas tem mais de 18 anos.
# b) Quantos homens foram cadastrados.
# c) Quantas mulheres tem menos de 20 anos.


from tkinter import N


contIdade = contM = contF = 0

while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    
    idade = int(input('Digite a idade da pessoa: '))
    sex = str(input('Digite o sexo da pessoa: [F/M] ')).upper().strip()[0]
    resposta = str(input('Deseja continuar: [S/N]? ')).upper().strip()[0]
    if sex != 'F' and sex != 'M':
        sex = str(input('Digite o sexo da pessoa: [F/M] ')).upper().strip()[0]
    if resposta != 'S' and sex != 'N':
        resposta = str(input('Deseja continuar: [S/N]? ')).upper().strip()[0]
    if idade > 18:
        contIdade+=1
    if sex == 'M':
        contM+=1
    if sex == 'F' and idade < 20:
        contF+=1
    if resposta == 'N':
        break
print('====== FIM DO PROGRAMA ======')
print('Total de pessoas com mais de 18 anos: {}'.format(contIdade))
print('Ao todo temos {} homens cadastrados'.format(contM))
print('E temos {} mulheres com menos de 20 anos'.format(contF))