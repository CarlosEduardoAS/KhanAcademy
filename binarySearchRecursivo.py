def binary_search(lista, elemento, min=0, max=None):
    if max == None:
        max = len(lista) - 1
    if max < min:
        return False
    else:
        meio = min + (max - min)//2
    if lista[meio] > elemento:
        return binary_search(lista, elemento, min, meio-1)
    elif lista[meio] < elemento:
        return binary_search(lista, elemento, meio+1, max)
    else:
        return meio


primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(binary_search(primos, 7))
