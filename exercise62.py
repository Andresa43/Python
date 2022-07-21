# Melhore o desafio061 , perguntando se ele quer mostrar mais alguns 
# termos. O programa encerra quando ele disser que quer mostrar 0 zero
# termos.

termos = 10
teste = 0
one_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))

while termos != 0:
    decimo = one_termo + (termos - 1)*razao
    print('{} ->'.format(one_termo), end= ' ')
    while decimo > one_termo:
        one_termo = one_termo + razao
        print('{} ->'.format(one_termo), end= ' ' )
    termos = int(input('\n Digite mais termos ou 0 para encerrar o programa: '))
    termos = termos+1
print('PROGRAMA ENCERRADO')
