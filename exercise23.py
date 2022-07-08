

num = float(input('Digite um número de 0 a 9999: '))


unidade = num // 1 % 10 
dezena = num // 10 % 10 
centena = num // 100 % 10 
milhar = num // 1000 % 10 

# unidade = int(str(int(num))[-1])
# dezena = int(str(int(num/10))[-1])
# centena = int(str(int(num/100))[-1])
# milhar = int(num/1000)

print('Unidade = {} Dezena = {} Centena = {} Milhar = {}'.format(unidade, dezena, centena, milhar))

