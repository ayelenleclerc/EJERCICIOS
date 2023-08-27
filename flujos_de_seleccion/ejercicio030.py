"""Escribir un programa que permita al usuario ingresar dos números enteros. La computadora debe indicar si el mayor es divisible por el menor.

(Un número entero a es divisible por un número entero b cuando el resto de la división entre a y b es 0)

"""
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 > num2:
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1

if mayor % menor == 0:
    print(f"El mayor {mayor} es divisible por el menor {menor}")
else:
    print(f"El mayor {mayor} no es divisible por el menor {menor}")
