
# Refaça o desafio051, lendo o primeiro e a razaõ de uma PA,
# mostrando os 10 primeiros termos da progressão usando a 
# estrutura while.



print('GERADOR DE PA')
print('-=' * 10)
one_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
cont = 1

while cont <= 10:
    print('{} ->'.format(one_termo), end= ' ')
    one_termo = one_termo + razao
    cont += 1
print('ACABOU')



# one_termo = int(input('Digite o primeiro termo da PA: '))
# razao = int(input('Digite a razao da PA: '))
# decimo = one_termo + (10 - 1)*razao 

# print('{} ->'.format(one_termo), end= ' ')
# while decimo > one_termo:
#     one_termo = one_termo + razao
#     print('{} ->'.format(one_termo), end= ' ')
# print('ACABOU!')

