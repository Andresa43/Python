# Melhore o desafio061 , perguntando se ele quer mostrar mais alguma 
# progressão. O programa encerra quando ele disser que quer mostrar 0 zero
# termos.

resposta = 'S'
while resposta == 'S':
        one_termo = int(input('Digite o primeiro termo da PA: '))
        razao = int(input('Digite a razao da PA: '))
        decimo = one_termo + (10 - 1)*razao 
        print('{} ->'.format(one_termo), end= ' ')
        while decimo > one_termo:
                one_termo = one_termo + razao
                print('{} ->'.format(one_termo), end= ' ' )
        resposta = str(input('\n Deseja fazer uma nova progressão? [S/0] ')).upper()
print('PROGRAMA ENCERRADO')   