"""Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor."""

numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
numero3 = int(input("Ingrese el tercer número entero: "))

numero_mayor = max(numero1, numero2, numero3)

print(f"El mayor es: {numero_mayor}")
