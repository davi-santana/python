from modulos import lista

def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista




# ******  Tire as  3 aspas simples (''') se quiser imprimir a sequência   ****** 
'''lista_ordenada = bubble_sort(lista)
print(f'Bubble sort:   {lista_ordenada}')
'''


