# Escreva um programa que leia um número n inteiro 
# qualquer e mostre na tela os n primeiros elementos 
# de uma sequencia de fibonacci




number = int(input('Digite um número inteiro: '))

cont = 0
sucessor = 1
anterior = 1
fibo = 0


while number != 0:
    number = number -1
    cont += 1
    if cont == 1:
        anterior = sucessor = 1
    else:
        fibo = anterior + sucessor
        sucessor = fibo 
        fibo = anterior + sucessor
    print(fibo)






