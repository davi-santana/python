''' Crie um programa em Python para calcular
o fatorial de um número dado pelo usuário.  '''

numero = int(input('Digite um numero para calcolar o seu fatorial: '))
fatorial = 1

while(numero > 1):
    fatorial = fatorial * numero
    numero = numero - 1
print ("O fatorial é {}".format(fatorial))
