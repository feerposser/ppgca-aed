
def get_pivot(lista, maior, menor):
    medio = (maior+menor)//2
    pivot = maior

    if lista[menor] < lista[medio]:
        if lista[medio] < lista[maior]:
            pivot = medio
        elif lista[menor] < maior:
            pivot = menor
    return pivot

import time

def partition(lista, inicio, fim):
    pivo = lista[0]
    up = inicio
    down = fim

    print('::',lista, down)

    print("\n--lista", lista, "\n--pivo=", pivo, "\n--down:", down, lista[down], "\n--up:", up, lista[up])
    while down > up:
        while True or up < len(lista):
            print('lista up', lista[up])
            print('pivo', pivo)
            if lista[up] > pivo:
                break
            up += 1
            print('++up', up, lista[up])

        while True or down > up:
            if lista[down] < pivo:
                break
            if down == 0:
                return pivo, pivo
            down -= 1
            print('++down', down, lista[down], down > up)

        print("muda o down", down, lista[down], "por up", up, lista[up])
        lista[up], lista[down] = lista[down], lista[up]
        up += 1
        down -= 1
        print("alteração:", lista)
    lista[0], lista[down] = lista[down], lista[0]
    return lista, down


def quicksort(lista, inicio, fim):
    if inicio < fim and len(lista) > 1:
        lista, pivo = partition(lista, inicio+1, fim)
        print("lista - pivo", lista, pivo)
        return quicksort(lista[inicio:pivo], inicio, pivo-1) + [pivo] + quicksort(lista[pivo+1:len(lista)-1], pivo+1, len(lista)-1)

    return lista


l = [44, 75, 23, 43, 55, 12, 64, 77, 33]
print(quicksort(l, 0, len(l)-1))