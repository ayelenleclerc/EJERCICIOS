"""Escribir un programa que muestre todos los números enteros del 1 al 5, y luego los mismos números pero en orden inverso.

"""
numeros = [1, 2, 3, 4, 5]

print("Al derecho :")
for numero in numeros:
    print(numero)

print("Al reves")
for numero in reversed(numeros):
    print(numero)
