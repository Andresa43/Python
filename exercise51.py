


One_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão dessa PA: '))
decimo = One_termo + (10 - 1)*razao


print('-'*12,'10 primeiros termos da PA', '-'*12)
for index in range(One_termo, decimo + razao, razao):
    print(index, end= ' -> ')
print('ACABOU!')


