from modulos import lista


for i in range(len(lista)):
      
   
    min_idx = i
    for j in range(i+1, len(lista)):
        if lista[min_idx] > lista[j]:
            min_idx = j
              
           
    lista[i], lista[min_idx] = lista[min_idx], lista[i]
  

print ("Sorted array")
for i in range(len(lista)):
    print(lista[i]), 
    