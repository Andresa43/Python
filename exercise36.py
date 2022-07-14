
house_money = float(input('Digite o valor da casa: R$'))
wage = float(input('Salário do comprador: R$'))
years = int(input('Quantos anos de financiamento?: '))

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
monthly = house_money/(years*12)
limit = wage*0.30

if monthly > limit:
    print('Seu empréstimo foi negado')
else:
    print('Empréstimo concedido!')
    # print('Parabéns! você poderá pagar R$ {:.2f} por mês'.format(monthly))
