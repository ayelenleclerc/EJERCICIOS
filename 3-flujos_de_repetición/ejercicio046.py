"""Escribir un programa que a partir de un número entero cant ingresado por el usuario permita cargar por teclado cant números enteros. La computadora debe mostrar cuál fue el mayor número y en qué posición apareció.
numero random = 0.0 .... 0.9999999999999..."""

# import random


# maximo = -float('inf')

# cant = random.randint(1, 99)
# for x in range(cant):
#   numero = random.randint(-1000,1000 )


from random import randint

posicion = 0
maximo = -float("inf")
cant = randint(1, 99)
for x in range(cant):
    numero = randint(-1000, 1000)
    print(f"Numero: {numero} Posicion: {x+1}")
    if numero > maximo:
        posicion = x + 1
        maximo = numero
print(f"Cantidad de numeros: {cant} Máximo: {maximo} posición: {posicion}")
