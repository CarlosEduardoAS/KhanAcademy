from random import randint


def gerador(num):
    lista = []
    for i in range(0, num):
        n = randint(0, 1000)
        if n not in lista:
            lista.append(n)
    return lista


def selection_sort(lista):
    fim = len(lista)
    for i in range(fim - 1):
        minimo = i
        for j in range(i+1, fim):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]


vetor = gerador(100)
selection_sort(vetor)
print(vetor)
