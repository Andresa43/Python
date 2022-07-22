
greater_weight = 0
less_weight = 0

for index in range (0, 5):
    weight = float(input('Digite o peso da pessoa: '))

    if index == 0:
        greater_weight = weight 
        less_weight = weight 
    else:
        if weight >  greater_weight:
            greater_weight = weight
        if less_weight > weight:
            less_weight = weight


print('Maior Peso = {} Menor Peso = {}'.format(greater_weight, less_weight))
