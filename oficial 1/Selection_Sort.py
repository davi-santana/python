from modulos import lista
import time

inicio = time.time()
def selectionSort(lista='lista'):
    for i in range(len(lista)):
        minimo = i
        for j in range(i+1, len(lista)):
            if lista[minimo] > lista[j]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]

selectionSort(lista)
for i in range(len(lista)):
    print(lista[i])

fim = time.time()
diferenca = fim - inicio
print(diferenca)


