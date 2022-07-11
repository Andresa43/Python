
from datetime import date 
    
year = int(input('Digite um ano ou coloque 0 para analisar o ano atual '))

if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano {} É bissexto'.format(year))
else:
    print('O ano {} NÃO é bissexto'.format(year))
