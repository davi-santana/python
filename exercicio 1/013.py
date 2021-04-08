''' Escreva o programa que conte a quantidade
de números pares e ímpares para uma série
de valores inteiros.
Exemplo de série:
(1, 2, 3, 4, 5, 6, 7, 8, 9)
Ímpares: 5
Pares: 4 '''

num = [[], []]
valor = 0

for lista in range(1, 9):
    if lista %2 ==0:
        num[0].append(valor)
    else:
        num[1].append(valor)
    print(lista, end=",") 
print('{num}')''' não finalizada'''
       