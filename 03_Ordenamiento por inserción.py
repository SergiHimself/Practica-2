# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:23:48 2023

@author: sergi
"""

def insertion_sort(arr):
    """
    Implementación del método de ordenamiento por inserción.

    Recibe como parámetro una lista 'arr' de elementos comparables y devuelve la lista ordenada.
    """
    # Obtener la longitud de la lista.
    n = len(arr)

    # Iterar a través de todos los elementos de la lista a partir del segundo elemento.
    for i in range(1, n):

        # Almacenar el valor actual en una variable temporal.
        current_val = arr[i]

        # Comparar el valor actual con los valores anteriores en la lista ordenada.
        j = i - 1
        while j >= 0 and arr[j] > current_val:
            arr[j+1] = arr[j]
            j -= 1

        # Insertar el valor actual en su posición correcta en la lista ordenada.
        arr[j+1] = current_val

    # Devolver la lista ordenada.
    return arr

# Definir la lista de colores.
colores = ["rojo", "verde", "azul", "amarillo", "morado"]

# Ordenar la lista de colores utilizando el método de ordenamiento por inserción.
colores_ordenados = insertion_sort(colores)

# Imprimir la lista ordenada de colores.
print(colores_ordenados)
