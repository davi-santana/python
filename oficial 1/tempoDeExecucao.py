import time
from modulos import lista
from bubble_sort import bubble_sort
from Insertion_Sort import insertion_sort
from Selection_Sort import  selectionSort


print("*************** Buble Sort ***************")
tempoInicial1 = time.time()
bubble_sort(lista)
print('Duração: %0.5f' % (time.time() - tempoInicial1))

print("\n*************** Insertion Sort ***************")
tempoInicial2 = time.time()
insertion_sort(lista)
print('Duração: %0.5f' % (time.time() - tempoInicial2))

print("\n*************** Selection Sort ***************")
tempoInicial3 = time.time()
selectionSort(lista)
print('Duração: %0.4f' % (time.time() - tempoInicial3))

'''Justifique qual teve o melhor desempenho em sua opinião.'''

''' Depois de varios teste realizados 
    na minha opinião o que teve melhor desempenho
    e o Insertion sort porque ele e o que apresentou
    mais rapidez em ordenar um array de 50k de numeros aleatorios ''' 


