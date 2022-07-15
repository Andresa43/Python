n = int(input('Digite um número inteiro: '))
print('-' *12)

for c in range(0, 11):
    print('{} x {:2} = {}'. format(n, c, n*c))
