cont = 0
n = int(input('Digite um número inteiro: '))
for c in range (1, n+1):
    if n%c == 0:
        cont += 1
        print(' \033[32m{}'.format(c), end= ' ') 
    if n%c != 0:
        print('\033[31m{}'.format(c), end= ' ')
    
if n == 2:
    print('\n O número {} foi divisível {} vezes \n E por isso É PRIMO!'.format(n, cont))
elif n%2 == 0:
    print('\n O número {} foi divisível {} vezes \n E por isso NÃO É PRIMO!'.format(n, cont))
else:
    print('\n O número {} foi divisível {} vezes \n E por isso É PRIMO!'.format(n, cont))


