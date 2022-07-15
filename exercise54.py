from datetime import date
current_year = date.today().year
menor = 0 
maior = 0 

for c in range (0, 7):
    birth_date = int(input('Digite o ano de nascimento: '))
    if current_year - birth_date >= 18:
        maior += 1
    else:
        menor += 1
print('{} Pessoas Atingiram a maioridade e {} NÃO atingiram a maioridade'.format(maior, menor))
