"""Escribir un programa que permita ingresar la cantidad de invitados a una fiesta y la cantidad de asientos disponibles en el salon. Debes indicar si alcanzan los asientos, Si los asientos no alcanzaran indicar cuántos faltan para que todos los invitados puedan sentarse.

"""


cantidad_invitados = int(input("Cantidad de invitados:"))
cantidad_asientos = int(input("Cantidad de asientos:"))

faltantes = cantidad_invitados - cantidad_asientos

if cantidad_invitados >= cantidad_asientos:
    print(f"Faltan {faltantes} asientos para que todos los invitados puedan sentarse")
else:
    print(f"Estan todos los invitados sentados")
