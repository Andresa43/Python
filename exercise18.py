
import math 

ang = float(input('Digite um ângulo qualquer: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print('O ângulo de {} tem Seno = {:.2f} / Cosseno = {:.2f} / Tangente = {:.2f}'.format(ang,sen, cos, tang))

