import random
import numpy as np
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


inicio = time.time()

quantidade = int(random.randint(10000, 1000000))
num = []
for x in range(quantidade):
    num.append(random.randint(20000, 2000000))

bubble_sort(num)
fim = time.time()

t1 =  fim - inicio

#BubbleSort
array_size = random.randint(10 ** 4, 10 ** 6)

array = np.random.randint(2, 2 * 10 ** 6, array_size)


def mergeSort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]

        mergeSort(sub_array1)
        mergeSort(sub_array2)

        i = j = k = 0

        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1

        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1

        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1


start_time = time.time()

mergeSort(array)

t2 = (time.time() - start_time)

#MergeSort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)
start = time.time()
qtd = int(random.randint(10000, 1000000))
num = []
for x in range(qtd):
    num.append(random.randint(20000, 2000000))
quick_sort(num)
end = time.time()

t3 = end - start
#QuickSort
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    elif value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    if root is None or root.value == value:
        return root
    elif root.value < value:
        return search(root.right, value)
    else:
        return search(root.left, value)

# gerando uma árvore binária aleatória
start_t = time.time()
n = random.randint(10000, 1000000)
root = None
for i in range(n):
    root = insert(root, random.randint(20, 2000000))

# buscando um número na árvore binária
x = 100000
result = search(root, x)
end_t = time.time()

# imprimindo o resultado e o tempo de execução
if result is None:
    achou = 0 #nao achou
else:
    achou = 1 #achou
t4 = end_t - start_t
#Arvore Binaria
import random
import time

def binary_search(lst, x):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# gerando uma lista aleatória com tamanho aleatório
start_tim = time.time()
n = random.randint(10000, 1000000)
lst = [random.randint(20, 2000000) for _ in range(n)]

# ordenando a lista para a busca binária
lst.sort()

# buscando um número na lista
x = 5000
if x < lst[0] or x > lst[-1]:
    print(f"O número {x} não está na lista.")
    print(f"Tempo de execução: {end_time - start_time:.6f} segundos")
else:
    result = binary_search(lst, x)
    end_tim = time.time()
    if result == -1:
       acho = 0#nao achou
    else:
        acho = 1 #achou
t5 = end_tim - start_tim

print("-_-_-_-_- Contadores de tempo -_-_-_-_-")
print("\t\t BubbleSort:",format(t1, '.4f'),"s\n\t\t MergeSort:",format(t2, '.4f'),"s\n\t\t QuickSort:",format(t3, '.4f'),"s\n\t\tArvore Binaria:",format(t4, '.4f'),"s\n\t\tBusca Binaria:",format(t5, '.4f'),"s")