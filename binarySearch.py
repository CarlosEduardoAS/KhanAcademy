def binary_search(target, array):
    array.sort()
    print(array)
    minimo = 0
    maximo = len(array) - 1
    while minimo <= maximo:
        chute = (minimo + maximo) // 2
        if array[chute] == target:
            return print(f'O número {n} está na posição {chute} (ou {chute+1}) na lista.')
        elif array[chute] < target:
            minimo = chute + 1
        else:
            maximo = chute - 1
    return print(f'O número {n} não está presente na lista.')


primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
n = int(input('Buscar número primo: '))
binary_search(n, primos)
