from time import time
from Selection_Sort import selection_sort

instante_inicial = time()
instante_final = time()
diferenca = (instante_final - instante_inicial) * 1000

print(f'O tempo de execução do calculo do fatorial foi de: {diferenca:.2f} ms')