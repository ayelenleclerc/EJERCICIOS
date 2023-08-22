"""Escribir un programa que permita ingresar dos números enteros e indicar si el primero es mayor, menor o igual al segundo.

"""
numero1 = int(input("Ingrese un número entero: "))
numero2 = int(input("Ingrese otro número entero: "))

if numero1 == numero2:
    print(f"Los números {numero1} y {numero2} son iguales")
elif numero1 > numero2:
    print(f"El número {numero1} es mayor que el número {numero2}")
else:
    print(f"El número {numero1} es menor que el número {numero2}")
