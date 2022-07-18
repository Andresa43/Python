

# num = []
maior = 0
menor = 0

for c in range (0, 5):
    peso = float(input('Digite o peso da pessoa: '))
    # num.append(peso)

    if c == 0:
        maior = peso 
        menor = peso 
    else:
        if peso > maior:
            maior = peso
        if menor > peso:
            menor = peso
print('Maior {} Menor {}'.format(maior, menor))
