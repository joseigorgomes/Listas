class OrdenaLista():

    def ordenaDecrescente(lista):                   
        for i in range(1, len(lista)): 
            key = lista[i] 

            j = i-1
            while j >=0 and key < lista[j] : 
                lista[j+1] = lista[j] 
                j -= 1
            lista[j+1] = key 

    def ordenaCrescente(lista):
        for j in range(1,len(lista)):
            key = lista[j]

            i = j - 1
            while i >= 0 and lista[i] < key:
                lista[i+1] = lista[i];
                i-=1
            lista[i+1] = key
