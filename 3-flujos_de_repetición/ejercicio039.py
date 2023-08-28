"""Escribir un programa para calcular e imprimir la suma de los números comprendidos entre 42 y 176

"""

suma = 0
for numero in range(42, 177):
    suma += numero
    print(f"La suma de los números comprendidos entre {numero} y 176 es:{suma}")
