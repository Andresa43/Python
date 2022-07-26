# faça um programa que mostra a tabuada de vários números, um de cada vez, para cada valor 
# digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.



while True:
    print('-'*40)
    number = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*40)
    if number < 0:
        break
    cont=0
    while cont < 10:
        cont+=1
        print('{} x {:2} = {}'. format(number, cont, number*cont))
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')