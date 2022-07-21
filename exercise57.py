# Faça um programa que leia o sexo de uma pessoa, mas só
# aceite os valores 'M' ou 'F'. Caso esteja errado, peça
# a digitação novamente até ter um valor correto.

sex = ' '
while sex != 'M' and sex != 'F':
    sex = str(input('Digite o sexo da pessoa [F/M]: ')).upper()
print('O seu sexo é {}'.format(sex))