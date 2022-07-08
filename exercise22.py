
nomeCompleto = str(input('Digite o seu nome completo: ')).strip()

# strip tira o espaço no inicio e no final da frase
# split junta as palavras e as transforma em novos index 

upper = nomeCompleto.upper()
lower = nomeCompleto.lower()
letters = len(nomeCompleto) - nomeCompleto.count(' ') 
split = nomeCompleto.split()
firtname = split[0]
countletter = len(firtname)


print('Nome maiúsculo:', upper)
print('Nome Minúsculo:', lower)
print('Tem ao todo {} letras'.format(letters))
print('Seu primeiro nome é {} e ele tem {} letras'. format(firtname, countletter))

