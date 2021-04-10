import csv
from collections import OrderedDict


with open ('/home/davi/Área de Trabalho/cursos-prouni2.csv', "r") as arquivo_csv:
    lista = csv.reader(arquivo_csv)
    
    r = []
    [r.append(i) for i in lista if not r.count(i)]

    print(sorted(r))
    