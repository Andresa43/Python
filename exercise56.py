media = 0
s = 0
for c in range (0, 4):
    name = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade:  '))
    media += idade/4
    sex = str(input('Qual o seu sexo? F/M: ')).upper()
    if sex == 'F' and idade < 20:
        s = c + 1

print('Media do grupo {}'.format(media))
print('Mulheres que tem menos de 20 anos é igual a {}'.format(s))