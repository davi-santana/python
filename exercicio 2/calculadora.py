'''
1. Você precisa criar uma calculadora para executar as quatro operações básicas, adição, subtração, multiplicação e divisão.
2. Como usuário, eu desejo escolher o tipo deoperação que será executada.
3. Como usuário eu desejo informar os dois valores utilizados na operação.
4. Como usuário desejo visualizar o resultadoda seguinte maneira: 4 + 3 = 7 ou 3 / 2 = 1.5.

Limitações:
(a) O programa deve ser executado em um loop, que só será encerrado caso o usuário deseje.
(b) Após escolher a operação, o usuário deve inserir os valores que serão utilizados na operação.
(c) Após a inserção dos valores, o resul-tado deve ser exibido, como descrito no item 4.
(d) Cada operação deve ser executada em uma função.
(e) Deve existir uma função responsávelpela leitura dos dados.  '''

def adicao(num1, num2):
   return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

def exponenciacao(num1, num2):
    return num1 ** num2




sair = False
while sair == False:
    print('******* calculadora em Python *******')

    print('\n Escolha o tipo de operação que será executada:\n ')

    print('1 | adição')
    print('2 | subtração ')
    print('3 | multiplicação')
    print('4 | divisão ')
    print('5 | exponenciação ')

    operação = input('Qual é a operação? ')
    numero1, numero2 = [float(x) for x in input("Entre com 2 valores, separados com espaço: ").split()]
   # numero2 = float(input('Digite o segundo valor: '))
    
    num1 = numero1
    num2 = numero2

    if operação ==  '1':
        print(f'{numero1} + {numero2} =  {adicao(num1, num2)}')

    elif operação == '2':
        print(f'{numero1} - {numero2} = {subtracao(num1, num2)}')

    elif operação == '3':
        print(f'{numero1} * {numero2} = {multiplicacao(num1, num2)}')

    elif operação == '4':
        print(f'{numero1} / {numero2} = {divisao(num1, num2)}')

    elif operação == '5':
        print(f'{numero1} elevado {numero2} = {exponenciacao(num1, num2)}')
    else:
        print('ERRO')
    
    


    sairTemp = input('Deseja fazer outra operação? (s/n)\n')
    if sairTemp == 'n':
        sair = True
    elif sairTemp == 'N':
        sair = True
    
    #criar um dicionario aninhado, onde a chave e a região, e os valoresa, os estados pertencentes a regiao.
    



   
