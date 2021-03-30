from random import randint


def gerador(num):
    lista = []
    for i in range(0, num):
        n = randint(0, 1000)
        if n not in lista:
            lista.append(n)
    return lista


def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    lado_esquerdo = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])
    return merge(lado_esquerdo, lado_direito)


def merge(lado_esquerdo, lado_direito):
    if not lado_esquerdo:
        return lado_direito
    if not lado_direito:
        return lado_esquerdo
    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)
    return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])


vetor = gerador(100)
print(merge_sort(vetor))
