
n = float(input('Digite o primeiro número: '))
n1 = float(input('Digite o segundo número: '))
n2 = float(input('Digite o terceiro número: '))
menor = n 
maior = n

if n1<n and n1<n2:
    menor = n1 
if n2<n1 and n2<n:
    menor = n2

if n1>n and n1>n2:
    maior = n1 
if n2>n1 and n2>n:
    maior = n2

print('Entre os número {}, {} e {} O menor valor é: {} E o maior valor é: {}'.format(n, n1, n2, menor, maior))