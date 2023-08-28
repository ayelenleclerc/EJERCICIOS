"""Escribir un programa que permita ingresar dos numeros enteros a y b.
con a <=b 
El programa debe mostrar:

La suma de los numeros pares entre a y b.
El producto de los numeros impares entre a y b.
"""
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

while a > b:
    print(f" Error, el segundo numero debe ser mayor que el primero")
    b = int(input("Ingrese el segundo numero: "))


suma_pares = 0
producto_impares = 1

for numero in range(a, b + 1):
    if numero % 2 == 0:
        suma_pares += numero
    else:
        producto_impares *= numero

print(f"La suma de los numeros pares entre {a} y {b} es: {suma_pares}")
print(f"El producto de los numeros impares entre {a} y {b} es: {producto_impares}")
