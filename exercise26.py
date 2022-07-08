phrase = str(input('Digite uma frase qualquer: ')).strip().upper()

count = phrase.count('A')

firt = phrase.find('A') + 1

last = phrase.rfind('A') + 1

print('Aparece {} vezes a letra A'.format(count))

print('Aparece pela primeiza vez na posição {} a letra A'.format(firt))

print('Aparece na última vez na posição {} a letra A'.format(last))


