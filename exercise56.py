
average = 0
maior = 0 
saveName = ''
sumF = 0

for index in range (0, 4):
    print('------------- {}° Pessoa -------------------'.format(index+1))
    name = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade:  '))
    average += idade/4
    sex = str(input('Qual o seu sexo? [F/M:] ')).upper()
    
    if sex == 'F' and idade < 20:
        sumF = index + 1
    
    if index == 0 and sex == 'M':
        maior = idade
        saveName = name
    else:
        if idade > maior and sex == 'M':
            maior = idade
            saveName = name
    


print('Media do grupo é de {} anos'.format(average))
print('Mulheres que tem menos de 20 anos é igual a {}'.format(sumF))
print('O homem mais velho tem {} anos e o nome dele é {}'.format(maior, saveName))

