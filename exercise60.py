
# Faça um programa que leia um número qualquer e mostre 
# o seu fatorial.



number = int(input('Digite um número qualquer: '))
cont = number

# print('{}! = {}'.format(number, number), end= ' ')
# while cont != 1:
#     cont = cont -1
#     number = number * cont
#     print('x {}'.format(cont), end= ' ')   
# print(' = {}'.format(number))

print('{}! = {}'.format(number, number), end= ' ')
for index in range(number-1, 0, -1):
    number = number*index
    print('x {}'.format(index), end= ' ')

print('= {}'.format(number), end= ' ')
