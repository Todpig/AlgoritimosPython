import random
import time

def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    i, j = 0, 0
    for k in range(inicio, fim):
        if i >= len(left):
            lista[k] = right[j]
            j = j + 1
        elif j >= len(right):
            lista[k] = left[i]
            i = i + 1
        elif left[i] < right[j]:
            lista[k] = left[i]
            i = i + 1
        else:
            lista[k] = right[j]
            j = j + 1
any_numbers = random.sample(range(1, 10000000), 9999999)

if __name__ == '__main__':
    lista = any_numbers
    
    inicio = time.time()
    mergesort(lista)
    fim = time.time()
    
    tamlista = len(lista)
    print("O maior elemento da lista é: ", lista[tamlista-1])
    print('O tempo de execução é: ', fim - inicio)