from cmath import sqrt
import math 

ang = float(input('Digite um ângulo qualquer: '))

sen = math.sin(ang)
cos = math.cos(ang)
tang = math.tan(ang)

print('Seno = {:.2f} / Cosseno = {:.2f} / Tangente = {:.2f}'.format(sen, cos, tang))

