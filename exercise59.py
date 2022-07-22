from time import sleep


number_one = float(input('Digite o primeiro valor: '))
number_two = float(input('Digite o segundo valor: '))
choice = 0
while choice != 5:
    print('=-'*20)
    print(''' Opções: 
    [1] SOMAR
    [2] MULTIPLICAR 
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
     ''')
    choice = int(input('Digite a sua escolha: '))
    print('-='*20)
    if choice == 1:
        print('Soma dos números {} e {} é igual {}'.format(number_one, number_two, number_one+number_two))
    elif choice == 2:
        print('Multiplicação dos números {} e {} é igual {}'.format(number_one, number_two, number_one*number_two))
    elif choice == 3:
        if number_one > number_two:
            print('O número {} é maior que o número {}'.format(number_one, number_two))
        else:
            print('O número {} é maior que o número {}'.format(number_two, number_one))
    elif choice == 4:
        number_one = float(input('Digite o primeiro valor: '))
        number_two = float(input('Digite o segundo valor: '))
    elif choice > 5:
        print('Opção inválida. Tente novamente')
print('Finalizando...')
sleep(3)
print('Fim do programa! Volte sempre!')
