''' Construa um algoritmo que, tendo como da-
dos de entrada dois pontos quaisquer no
plano, P(x1,y1) e P(x2,y2), escreva a dis-
tância entre  eles. A fórmula que efetua tal
cálculo é:
p
d = (x 2 − x 1 ) 2 + (y 2 − y 1 ) 2
Os valores devem ser informados pelo usuário '''


import math

x1 = float(input("Digite o valor de x1:\n"))
y1 = float(input("Digite o valor de y1:\n"))
x2 = float(input("Digite o valor de x2:\n"))
y2 = float(input("Digite o valor de y2:\n"))

d = ((x2 - x1)**2 + (y2 - y1)**2)
raiz = math.sqrt(d)

print (raiz)