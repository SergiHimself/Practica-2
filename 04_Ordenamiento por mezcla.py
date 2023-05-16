# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:50:36 2023

@author: sergi
"""

def merge_sort(arr):
    """
    Implementación del método de ordenamiento por mezcla (Merge Sort).

    Recibe como parámetro una lista 'arr' de elementos comparables y devuelve la lista ordenada.
    """
    # Definir la función recursiva que divide la lista en mitades hasta que sólo quede un elemento.
    def merge_sort_rec(arr):
        # Caso base: si la lista tiene uno o cero elementos, ya está ordenada.
        if len(arr) <= 1:
            return arr

        # Encontrar el punto medio de la lista.
        mid = len(arr) // 2

        # Dividir la lista en dos mitades.
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Llamar recursivamente a la función para ordenar las dos mitades.
        left_half_sorted = merge_sort_rec(left_half)
        right_half_sorted = merge_sort_rec(right_half)

        # Combinar las dos mitades ordenadas en una lista ordenada.
        result = []
        i = j = 0
        while i < len(left_half_sorted) and j < len(right_half_sorted):
            if left_half_sorted[i] < right_half_sorted[j]:
                result.append(left_half_sorted[i])
                i += 1
            else:
                result.append(right_half_sorted[j])
                j += 1

        # Añadir los elementos restantes de la mitad izquierda o derecha, si los hay.
        result.extend(left_half_sorted[i:])
        result.extend(right_half_sorted[j:])

        return result

    # Llamar a la función recursiva para ordenar la lista 'arr'.
    return merge_sort_rec(arr)

# Definir la lista de colores.
colores = ["rojo", "verde", "azul", "amarillo", "morado"]

# Ordenar la lista de colores utilizando el método de ordenamiento por mezcla (Merge Sort).
colores_ordenados = merge_sort(colores)

# Imprimir la lista ordenada de colores.
print(colores_ordenados)

