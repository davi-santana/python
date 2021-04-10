import time
from modulos import lista
from bubble_sort import bubble_sort


t1 = time.time()

bubble_sort()
tempoExec = time.time() - t1

print("Tempo de execução: {} segundos".format(tempoExec))

