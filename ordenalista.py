class OrdenaLista():

    def ordenaDecrescente(lista):
        auxiliar = 0
        for i in range(len(lista)):
            for j in range(len(lista)):
                if lista[i] > lista[j]:
                    auxiliar = lista[j]
                    lista[j] = lista[i]
                    lista[i] = auxiliar


    def ordenaCrescente(lista):
        auxiliar = 0
        for i in range(len(lista)):
            for j in range(len(lista)):
                if lista[i] < lista[j]:
                    auxiliar = lista[j]
                    lista[j] = lista[i]
                    lista[i] = auxiliar