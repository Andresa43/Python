
one_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
decimo = one_termo + (10 - 1)*razao 
resposta = ''


print('{} ->'.format(one_termo), end= ' ')
while decimo > one_termo:
    one_termo = one_termo + razao
    print('{} ->'.format(one_termo), end= ' ' )
print('\n')

resposta = str(input('Deseja mostrar mais termos? [S/0] ')).upper()
if resposta == 'S':
    while decimo > one_termo and resposta == 'S':
        decimo = one_termo + (10 - 1)*razao 
        one_termo = int(input('Digite o primeiro termo da PA: '))
        razao = int(input('Digite a razao da PA: '))
        one_termo = one_termo + razao
        print('{} ->'.format(one_termo), end= ' ' )
else:
    ('PROGRAMA ENCERRADO')

