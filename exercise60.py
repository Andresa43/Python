
# Faça um programa que leia um número qualquer e mostre 
# o seu fatorial.

number = int(input('Digite um número para calcular o seu Fatorial: '))
cont = number
factorial = 1

print('Calculando {}! ='.format(number), end= ' ')
while cont > 0:
    print('{}'.format(cont), end= ' ')
    print('x' if cont > 1 else '=', end= ' ')
    factorial *= cont #factorial = factorial * cont
    cont -= 1   #cont = cont -1
print(factorial)


#  ------------------------ Questão utilizando while---------------------------
# print('Calculando {}! = {}'.format(number, number), end= ' ')
# while cont != 1:
#     cont -= 1   #cont = cont -1
#     number = number * cont
#     print('x {}'.format(cont), end= ' ')   
# print(' = {}'.format(number))

# -----------------------Questão utilizando for ------------------------------

# print('{}! = {}'.format(number, number), end= ' ')
# for index in range(number-1, 0, -1):
#     number = number*index
#     print('x {}'.format(index), end= ' ')

# print('= {}'.format(number), end= ' ')

