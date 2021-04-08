
print('\n*************** criação de tuplas ************')
my_tupla = (1, 3, 5, 7, 9, 12, 18, 20 )
print ('tupla: ', my_tupla)
print ('tupla: ',type (my_tupla))
print('\n*************** convertendo lista em tupla ************')
my_lista = [2, 4, 6]
my_tupla = tuple(my_lista)

print('minha lista', my_lista)
print('type of my_list:', type(my_lista)) 
print('my tuple', my_tupla)
print('type pf my_tuple', type(my_tupla))

print('\n*************** imprimindo itens na lista ************')

print('my_tuple[2:6}', my_tupla[2 :6])
print('minha tupla[2:6}', my_tupla[::-1]) #imprime reverso

tp3 = (1, 'Davi', -856, 855)
print(f'tp3 contente{(tp3)}')

frutas = ('maçã', 'melancia', 'pera', 'laranga', 'uva', 'melão',)

for x in enumerate (frutas): #enumerando lista e tuplas
    print(f'\t{x}')
print('-' * 25)

print('*************** tupla dentro de tupla ************')
tuple1 = (1,2,3,4,5)
tuple2 = ('marcos', 'davi', 'joao')
tupe3 = (42, tuple1, tuple2, 5.5)
print(tupe3)


print('*************** listas ************')
teste = [1, 2, 3, 4, 5]
for b in teste:
    print(b)

voweltuple = ('a', 'b', 'c', 'd', 'y')
print(teste)
print('\n*************** ultimo elemento da lista ************')
print(f'last element of the teste lista: {teste[len(teste)-1]}')
print(f'last element of the teste lista: {teste[-1]}')

print('\n*************** inserir elementos na lista ************')


print('\n*************** inserir elementos na lista ************')

print('\n*************** criando conjuntos ************')
#itens repetidos nao aparecem
fruits = {'aple', 'aple', 'banana', 'pera', 'pera' }
print(fruits)
#adicionar itens no conjuntis
fruits.add('melao')
print(fruits)

print(len(fruits))

#pega o maior valor
print(max(fruits))

#pega o valor minimo
print(min(fruits))


print('*************** dicionario ************')

estadosCapitais =  {'mato grosso' : 'cuiabá',
                    'Minas Gerais' : 'Belo Horizonte',
                    'Maranhão' : 'sao luiz',
                     'mato grosso do sul ' : 'Campo Grande' 
                     }
print(estadosCapitais)

dict_01 = dict(mg='belo horizonte', rj='rio de janeiro', sp= 'sao paulo')