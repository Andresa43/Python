print('-='*20)
print('Analisando de Triângulo')
print('-='*20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Primeiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r2 == r3:
        print('Os seguimentos acima PODEM formar um Triângulo Equilátero')
    elif r1 != r2 and r2 != r3:
        print('Os seguimentos acima PODEM formar um Triâgulo Escaleno')
    else: 
        print('Os seguimentos acima PODEM formar um Triângulo Isósceles')
else:
    print('Os seguimentos acima PODEM formar um Triângulo')
