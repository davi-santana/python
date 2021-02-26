#********Praticando em casa**********

#if else elif
'''
login = input("Digite o seu login: ")
senha = input("Digite sua senha: ")
if login == "userpy" and senha == "teste123":
    print("Bem vindo userpy01")
elif login == "poofMestre" and senha == "8928":
    print("Bem vindo poofMestre")
else:
    print("login falhou, verifique a sua senha e tente novamente")
'''

#**********Estrutura de repetição***********

'''>>> list(range(10)) #Gera uma sequência de 0 à 9.
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1)11) #Gera uma sequência de 1 à 11.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(0,30,5)) #Gera uma sequência de 0 à 30 com step = 5.
[0, 5, 10, 15, 20, 25]
>>> list(range(0,-10,-1)) #Gera uma sequência numérica negativa.
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> list(range(0)) )) #Gera uma lista vazia.'''

contagem = 0
#range sequencia numerica
for contagem in range(1,10):
    print (contagem)
while(contagem < 10):
    print(contagem)
    contagem = contagem +1
    