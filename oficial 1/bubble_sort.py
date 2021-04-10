from modulos import lista
import  time


def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


#print(f'Unordered: {lista}')


lista_ordenada = bubble_sort(lista)
print(f'Bubble sort:   {lista_ordenada}')

tempoInicial = time.time()
bubble_sort(lista)
print("--- %s segundos ---" % (time.time() - tempoInicial))

