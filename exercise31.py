distance = float(input('Digite a distância em Km: '))

if distance <= 200: 
    preco = distance*0.50
    print('Preço da passagem = {}'. format(preco))
else: 
    preco = distance*0.45
    print('Preço da passagem = {}'. format(preco))
