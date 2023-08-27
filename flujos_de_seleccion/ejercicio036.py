"""Escribir un programa que permita ingresar dos números enteros y la operación a realizar('+', '-', '*', '/'). Debe mostrarse el resultado para la operación ingresada. Considerar que no se puede dividir por cero (en ese caso mostrar el texto 'ERROR').

"""
num1 = int(input("Ingrese un número entero: "))
operacion = input("Ingrese la operación (+, -, *, /): ")
num2 = int(input("Ingrese otro número entero: "))


if operacion == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operacion == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operacion == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operacion == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("ERROR")
