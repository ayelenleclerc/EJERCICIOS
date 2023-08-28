"""Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad de km que desea recorrer el usuario.

Tiene la siguiente tarifa:

Viaje mínimo $50
Si recorre entre 0 y 10km: $20/km
Si recorre 10km o más: $15/km
Escribir un programa que permita ingresar la cantidad de km que desea recorrer el usuario y muestre el precio del viaje.

"""
VIAJE_MINIMO = 50

km = int(input("Ingrese la cantidad de km recorridos: "))

if km <= 10:
    precio = VIAJE_MINIMO + (km * 20)
else:
    precio = VIAJE_MINIMO + (km * 15)

print(f"El precio del viaje es: ${precio}")
