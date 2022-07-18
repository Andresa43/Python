s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor: '.format(c)))
    cont += 1
    if n%2==0:
        s += n
print('Você informou {} números e a soma dos números pares foi {}'.format(cont, s))

