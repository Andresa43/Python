velocity = int(input('Digite a velocidade do carro em km/h: '))

if velocity > 80: 
    multa = (velocity - 80) * 7
    print('Você foi multado e deverá pagar R$ {} de multa'.format(multa))
