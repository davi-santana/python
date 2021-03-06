''' Crie um programa para simular um jogo de
dados. Dois deles serão lançados simultaneamente.
Ao executar o algoritmo, a primeira rodada
será disparada. O programa deve continuar
no loop e imprimir o valor dos dois dados até
o usuário indicar que não quer mais continuar. '''
''
from random import randint

print("Rolling the dices...")
print("The values are....")
dado1 = randint(1, 6)
dado2 = randint(1, 6)

print(dado1, dado2)



