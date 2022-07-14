note1 = float(input('Digite a primeira nota: '))
note2 = float(input('Digite a segunda nota: '))
average = (note1+note2)/2

print('Tirando {} e {} nas provas sua média é igual a {}'.format(note1, note2, average))
if average < 5:
    print('Aluno está \033[31m REPROVADO')
elif average >=5 and average < 7:
    print('Aluno está em \033[35mRECUPERAÇÃO')
else:
    print('Aluno está \033[32mAPROVADO')