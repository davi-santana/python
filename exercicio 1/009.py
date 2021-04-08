''' Crie um programa em Python que receba
um inteiro (n) e calcule o valor de n + nn
+ nnn 
O valor dado de n é 5
O resultado esperado: 615 '''

num = str(input('Digite um numero inteiro: '))

soma1 = num + num
soma2 = soma1 + num
somaFinal = int(num) + int(soma1) + int(soma2) 
print ('O resultado de {} + {} + {} é: {} ' .format(num, soma1, soma2, somaFinal))