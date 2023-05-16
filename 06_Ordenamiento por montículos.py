# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:57:54 2023

@author: sergi
"""

def heapify(arr, n, i):
    """
    Función auxiliar para crear un montículo maximo a partir de un arreglo dado.
    """
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
 
    # Verificar si el hijo izquierdo del nodo raíz es mayor que el nodo raíz
    if l < n and arr[i] < arr[l]:
        largest = l
 
    # Verificar si el hijo derecho del nodo raíz es mayor que el nodo raíz
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Cambiar el nodo raíz si es necesario
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
 
        # Recursivamente heapificar el subárbol afectado
        heapify(arr, n, largest)
 
 
def heap_sort(arr):
    """
    Función principal para ordenar un arreglo utilizando el método de ordenamiento por montículos.
    """
    n = len(arr)
 
    # Construir un montículo maximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # Extraer los elementos uno por uno
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

colores = ["rojo", "verde", "azul", "amarillo", "morado"]
heap_sort(colores)
print(colores)
