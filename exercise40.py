note1 = float(input('Digite a primeira nota: '))
note2 = float(input('Digite a segunda nota: '))
average = (note1+note2)/2

if average < 5:
    print('Aluno \033[31m REPROVADO')
elif average >=5 and average <= 6.9:
    print('Aluno na \033[35mRECUPERAÇÃO')
else:
    print('Aluno \033[32mAPROVADO')