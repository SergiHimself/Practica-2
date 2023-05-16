# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 13:59:29 2023

@author: sergi
"""

def bubble_sort(arr):
    """
    Implementación del método de ordenamiento burbuja.

    Recibe como parámetro una lista 'arr' de elementos comparables y devuelve la lista ordenada.
    """
    # Obtener la longitud de la lista.
    n = len(arr)

    # Iterar a través de todos los elementos de la lista.
    for i in range(n):

        # En cada iteración, se compara cada elemento con su sucesor.
        # Si están en el orden incorrecto, se intercambian.
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Intercambiar elementos.
                arr[j], arr[j+1] = arr[j+1], arr[j]

    # Devolver la lista ordenada.
    return arr

# Definir la lista de colores.
colores = ["rojo", "verde", "azul", "amarillo", "morado"]

# Ordenar la lista de colores utilizando el método de ordenamiento burbuja.
colores_ordenados = bubble_sort(colores)

# Imprimir la lista ordenada de colores.
print(colores_ordenados)
