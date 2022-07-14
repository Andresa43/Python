
house_money = float(input('Digite o valor da casa: '))
wage = float(input('Digite o valor do seu salário: '))
years = int(input('Digite a quantidade de anos que você irá pagar: '))

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
monthly = house_money/(years*12)
limit = wage*0.30

if monthly > limit:
    print('Seu empréstimo foi negado')
else:
    print('Parabéns! você poderá pagar R$ {:.2f} por mês'.format(monthly))
