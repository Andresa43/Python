from math import sqrt

catop = float(input('Digite o cateto oposto da hotenusa: '))
catadj = float(input('Digite o cateto adjacente da hotenusa: '))

hipotenusa = sqrt(catop ** 2 + catadj ** 2)

print('O comprimento da hipotenusa é: {:.2f}'.format(hipotenusa))