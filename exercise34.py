wage = float(input('Digite o seu salário: '))

if wage > 1250: 
    aumento = wage * 0.10 + wage
    print('Novo Salário com aumento: R$ {}'.format(aumento))
else:
    aumento = wage * 0.15 + wage
    print('Novo Salário com aumento: R$ {}'.format(aumento))

