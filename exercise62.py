# Melhore o desafio061 , perguntando se ele quer mostrar mais alguns 
# termos. O programa encerra quando ele disser que quer mostrar 0 zero
# termos.





one_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
cont = 1
termos = 10
total = 0

while termos != 0:
    total = total + termos
    while cont <= total:
        print('{} ->'.format(one_termo), end= ' ' )
        one_termo = one_termo + razao 
        cont += 1
    print('PAUSA')
    termos = int(input('\nDigite mais termos ou 0 para encerrar o programa: '))
print('Progressão finalizada com {} termos mostrados'.format(total))



# termos = 10
# one_termo = int(input('Digite o primeiro termo da PA: '))
# razao = int(input('Digite a razao da PA: '))

# while termos != 0:
#     decimo = one_termo + (termos - 1)*razao
#     while decimo > one_termo:
#         one_termo = one_termo + razao
#         print('{} ->'.format(one_termo), end= ' ' )
#     termos = int(input('\n Digite mais termos ou -1 para encerrar o programa: '))
#     termos = termos+1
# print('PROGRAMA ENCERRADO')


                   