import random 
import time

lista = random.sample(range(50_000), 10)

opcao = 0
sair = False
while sair == False:
    print ('Escolha a opção desejada\n')
    print('Bublle sort       [1]')
    print('Insertion sort    [2]')
    print('Selection sort    [3]')
    print('Tempo de execução [4]')

    opcao = int(input('\nQual é sua opção?'))
    if opcao == 1:
        def bubble_sort(lista):
            n = len(lista)
            for i in range(n - 1):
                for j in range(n - 1):
                    if lista[j] > lista[j + 1]:
                        lista[j], lista[j + 1] = lista[j + 1], lista[j]
            return lista

        lista_ordenada = bubble_sort(lista)
        print(f'Bubble sort:   {lista_ordenada}')
            
    elif opcao == 2:
        def insertion_sort(lista):
        
            n = len(lista)
            for i in range(1, n):
                insert_value = lista[i]
                j = i - 1
                while j >= 0 and lista[j] > insert_value:
                    lista[j + 1] = lista[j]

                    j -= 1

                lista[j + 1] = insert_value
            return lista

        lista_ordenada2 = insertion_sort(lista)
        print(f'Insertion Short:   {lista_ordenada2}')
    
    elif  opcao == 3:

        def selectionSort(lista):
            for i in range(len(lista)):
                minimo = i
                for j in range(i+1, len(lista)):
                    if lista[minimo] > lista[j]:
                        minimo = j
                lista[i], lista[minimo] = lista[minimo], lista[i]

        selectionSort(lista)
        for i in range(len(lista)):
            print(lista[i])
        
    elif opcao == 4:
        tempoInicial = time.time()
        selectionSort(lista)
        print("--- %s segundos ---" % (time.time() - tempo_inicial))

    else:
        print('Opçao invalida. tente novamente')
        print ('Fim Do programa!')

    sairTemp = input('Deseja fazer outra operação? (s/n)\n')
    if sairTemp == 'n':
        sair = True
    elif sairTemp == 'N':
        sair = True


    


