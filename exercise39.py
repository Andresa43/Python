from datetime import date

year = int(input('Digite o seu ano de nascimento:  '))

current_year = date.today().year

result = current_year - year

if result == 18:
    print('Você tem {}, está na idade de se alistar ao serviço militar'.format(result))
elif result < 18:
    print('Você tem {}, não está na idade de se alistar'.format(result))
    print('Faltam {} anos para você se alistar'.format(18-result))
else:
    print('Você tem {}, já passou da idade de se alistar'.format(result))
    print('Você passou do prazo há {} anos!'.format(result-18))
