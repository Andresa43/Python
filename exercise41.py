from datetime import date
from shutil import register_unpack_format

year = int(input('Digite o seu ano nascimento:'))

current_year = date.today().year

result = current_year - year 

if result <= 9:
    print('O Atleta tem {} anos'.format(result))
    print('Classificação: MIRIM')
elif result <= 14:
    print('O Atleta tem {} anos'.format(result))
    print('Classificação: INFANTIL')
elif result <= 19:
    print('O Atleta tem {} anos'.format(result))
    print('Classificação: JUNIOR')
elif result <= 25:
    print('O Atleta tem {} anos'.format(result))
    print('Classificação: SÊNIOR')
else: 
    print('O Atleta tem {} anos'.format(result))
    print('Classificação: MASTER')