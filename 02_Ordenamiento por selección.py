# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:20:23 2023

@author: sergi
"""

def selection_sort(arr):
    """
    Implementación del método de ordenamiento por selección.

    Recibe como parámetro una lista 'arr' de elementos comparables y devuelve la lista ordenada.
    """
    # Obtener la longitud de la lista.
    n = len(arr)

    # Iterar a través de todos los elementos de la lista.
    for i in range(n):

        # Encontrar el valor mínimo en la lista no ordenada.
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Intercambiar el valor mínimo con el primer elemento de la lista no ordenada.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # Devolver la lista ordenada.
    return arr

# Definir la lista de colores.
colores = ["rojo", "verde", "azul", "amarillo", "morado"]

# Ordenar la lista de colores utilizando el método de ordenamiento por selección.
colores_ordenados = selection_sort(colores)

# Imprimir la lista ordenada de colores.
print(colores_ordenados)
