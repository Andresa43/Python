# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual 
# foi o maior e o menor valores lidos. O programa deve perguntar ao usuário 
# se ele quer ou não continuar a digitar valores.

save = 0
higher_number = 0
smallest_number = 0
cont = 0
answer = 'S'

while answer == 'S':
    cont += 1
    numbers = int(input('Digite um número inteiro: '))
    save = save + numbers
    if cont == 1:
        higher_number = smallest_number = numbers 
    else:
        if numbers > higher_number:
            higher_number = numbers
        if numbers < smallest_number:
           smallest_number = numbers
    answer = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
print('Você digitou {} números e a média foi {:.2f}'.format(cont, save/cont))
print('Maior valor = {} e Menor valor = {}'.format(higher_number, smallest_number))









#  if index == 0:
#     greater_weight = weight 
#     less_weight = weight 
# else:
#     if weight >  greater_weight:
#         greater_weight = weight
#     if less_weight > weight:
#         less_weight = weight