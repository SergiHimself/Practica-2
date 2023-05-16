# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:48:16 2023

@author: sergi
"""

def quick_sort(arr):
    """
    Implementación del método de ordenamiento rápido (QuickSort).

    Recibe como parámetro una lista 'arr' de elementos comparables y devuelve la lista ordenada.
    """
    # Caso base: si la lista tiene menos de dos elementos, ya está ordenada.
    if len(arr) < 2:
        return arr

    # Seleccionar el primer elemento de la lista como pivote.
    pivot = arr[0]

    # Dividir la lista en dos sub-listas, una con los elementos menores que el pivote
    # y otra con los elementos mayores o iguales que el pivote.
    smaller = [x for x in arr[1:] if x < pivot]
    greater_or_equal = [x for x in arr[1:] if x >= pivot]

    # Ordenar recursivamente las sub-listas.
    smaller_sorted = quick_sort(smaller)
    greater_or_equal_sorted = quick_sort(greater_or_equal)

    # Combinar las sub-listas ordenadas junto con el pivote para obtener la lista ordenada completa.
    return smaller_sorted + [pivot] + greater_or_equal_sorted

# Definir la lista de colores.
colores = ["rojo", "verde", "azul", "amarillo", "morado"]

# Ordenar la lista de colores utilizando el método de ordenamiento rápido (QuickSort).
colores_ordenados = quick_sort(colores)

# Imprimir la lista ordenada de colores.
print(colores_ordenados)
