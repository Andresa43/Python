from datetime import date

year = int(input('Digite o seu ano de nascimento:  '))

current_year = date.today().year

result = current_year - year

if result == 18:
    print('Você tem {} anos, está na idade de se alistar ao serviço militar'.format(result))
elif result < 18:
    print('Você tem {} anos, não está na idade de se alistar'.format(result))
    print('Faltam {} anos para você se alistar'.format(18-result))
    print('Você deve se alistar em {}'.format(current_year + (18-result)))
else:
    print('Você tem {} anos, já passou da idade de se alistar'.format(result))
    print('Você passou do prazo há {} anos!'.format(result-18))
    print('Seu alistamento foi em {}'.format(current_year - (result-18)))
