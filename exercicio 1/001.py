''' Crie um programa para simular um jogo de
dados. Dois deles serão lançados simultaneamente.
Ao executar o algoritmo, a primeira rodada
será disparada. O programa deve continuar
no loop e imprimir o valor dos dois dados até
o usuário indicar que não quer mais continuar. '''
from random import randint

sair = False
while sair  == False:
    print("Rolling the dices...")
    print("The values are....")
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)

    print(dado1, dado2)
    sairTemp = input('Rolll the dices again? (y/n):')
    if sairTemp == 'n':
        sair = True
    elif sairTemp == 'N':
        sair = True
    
