"""  
Escribir un programa que solicite al usuario ingresar tres numeros enteros.El programa debe mostrar por pantalla el resultado de sumar los tres numeros de la siguiente manera: "[numero1] + [numero2] + [numero3] = [suma]".

Ejemplo: Si el usuario ingresa 1, 2 y 3, el programa debe mostrar por pantalla: "1 + 2 + 3 = 6".
"""

num1 = int(input("Ingrese el primer número a sumar: "))
num2 = int(input("Ingrese el segundo número a sumar: "))
num3 = int(input("Ingrese el tercer  y ultimo número a sumar: "))

print(f"{num1} + {num2} + {num3} = {num1 + num2 + num3}")
