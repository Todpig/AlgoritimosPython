import random
import time

primos = []

def verifica_primo(n):
    mult = 0
    for count in range(2,n):
        if (n % count == 0):
            mult += 1

    if(mult==0):
        primos.append(n)   

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
            verifica_primo(lista[k])
            j = j + 1
        elif j >= len(right):
            lista[k] = left[i]
            verifica_primo(lista[k])
            i = i + 1
        elif left[i] < right[j]:
            lista[k] = left[i]
            verifica_primo(lista[k])
            i = i + 1
        else:
            lista[k] = right[j]
            verifica_primo(lista[k])
            j = j + 1

any_numbers = random.sample(range(1, 1000000000), 1000000)

if __name__ == '__main__':
    lista = any_numbers
    
    inicio = time.time()
    mergesort(lista)
    fim = time.time()
    
    print('O tempo de execução é: ', fim - inicio)
    