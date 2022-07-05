km = float(input('Quantos Kilômetros rodados? '))
dia = int(input('Quantos dias alugados? '))

preço = km * 0.15 + dia * 60 

print('Preço Total a pagar R${:.2f}'.format(preço))


