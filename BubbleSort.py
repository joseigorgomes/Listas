def BubbleSort(lista1): # Do menor para o maior
    for i in range(len(lista1)):
        for k in range(len(lista1) - 1):
            if lista1[k] > lista1[k + 1]:
                lista1[k], lista1[k + 1] = lista1[k + 1], lista1[k]
    return lista1

def BubbleSort_reverse(lista2): # Do maior para o menor
    for i in range(len(lista2)):
        for k in range(len(lista2) - 1):
            if lista2[k] < lista2[k + 1]:
                lista2[k], lista2[k + 1] = lista2[k + 1], lista2[k]
    return lista2

lista1 = [7, 5, -1, 3, 1, 9, 4, 3, 7, 8, 2]
lista2 = [7, 5, -1, 3, 1, 9, 4, 3, 7, 8, 2]
BubbleSort = BubbleSort(lista1)
BubbleSort_reverse = BubbleSort_reverse(lista2)
print(BubbleSort)
print(BubbleSort_reverse)
