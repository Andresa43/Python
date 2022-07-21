
average = 0
older_age = 0 
saveName = ''
sumF = 0

for index in range (0, 4):
    print('----------------- {}° Pessoa -------------------'.format(index+1))
    name = str(input('Digite o seu nome: '))
    age = int(input('Digite a sua idade:  '))
    average += age/4
    sex = str(input('Qual o seu sexo? [F/M:] ')).upper()
    
    if sex == 'F' and age < 20:
       sumF += 1
    
    if index == 0 and sex == 'M':
        older_age = age
        saveName = name
    else:
        if age > older_age and sex == 'M':
            older_age = age
            saveName = name
    
print('A media de idade do grupo é de {} anos'.format(average))
print('Mulheres que tem menos de 20 anos é igual a {}'.format(sumF))
print('O homem mais velho tem {} anos e se chama {}'.format(older_age, saveName))

