# Faça um programa que leia o sexo de uma pessoa, mas só
# aceite os valores 'M' ou 'F'. Caso esteja errado, peça
# a digitação novamente até ter um valor correto.


sex = str(input('Digite o sexo da pessoa [F/M]: ')).upper().strip()[0]
while sex != 'M' and sex != 'F':
    sex = str(input('Dados inválidos. Por favor, informe o seu sexo: ')).upper()
print('Sexo {} registrado com sucesso'.format(sex))