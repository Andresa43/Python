

product = float(input('Qual o valor do produto?: '))
payment = int(input('Qual a forma de pagamento? \n 1 - à vista dinheiro/cheque \n 2 - à vista no cartão \n 3 - em até 2x no cartão \n 4 - 3x ou mais \n Digite o número correspondente: '))

if payment == 1:
    product = product - product*0.10
    print('Valor com 10% de desconto = R${}'.format(product))
elif payment == 2:
    product = product - product*0.05
    print('Valor com 5% de desconto = R${}'.format(product))
elif payment == 3:
    product = product/2
    print('Sua compra será parcelada em 2x de: R${}'.format(product))
else:
    totpac = int(input('Quantas parcelas?'))
    print('Serão aplicados 20% de juros')
    print('Sua compra será parcelada em {}x de R${:.2f} com JUROS'.format(totpac, (product*1.20)/totpac))
  
