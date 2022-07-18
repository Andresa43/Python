from datetime import date
current_year = date.today().year
larger = 0 
smaller = 0 

for c in range (0, 7):
    birth_date = int(input('Digite o ano de nascimento: '))
    if current_year - birth_date >= 18:
       larger += 1
    else:
       smaller += 1
print('{} Pessoas Atingiram a maioridade e {} NÃO atingiram a maioridade'.format(larger, smaller))
