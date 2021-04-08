# chama a função def declara nome e os nome dos parametros 

def print_msg(name, message = 'Live long and prosper'):
    ''' Imprime uma mensagem de boas vindar '''
    print(name, message)

name = input('seu nome: ')
print_msg('Davi')

def exp(base, expoente):
    return base ** expoente 
    

a = int(input('Digite a base: '))
base = a
b = int(input('Digite o expoente: '))
expoente = b

print(f'{a}  {2} = {exp(a,b)}')

'''def print_names(*args):
    for i, name in enumerate(args):
        print('{i} - welcome{name}')

print_names('davi', 'c', 'f', 'gh', 'jgjg', jfjfjf' )
'''



    