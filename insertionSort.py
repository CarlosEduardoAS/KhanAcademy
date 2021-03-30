from random import randint


def gerador(num):
    lista = []
    for i in range(0, num):
        n = randint(0, 1000)
        if n not in lista:
            lista.append(n)
    return lista


def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = chave


vetor = gerador(100)
insertion_sort(vetor)
print(vetor)
