"""Escribir un programa que permita ingresar una edad (entre 1 y 120 años), un género ('F'para mujeres, 'M' para hombres) y un nombre. En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido), informar tal situación indicando el nombre de la persona. Si los datos están bien ingresados el programa debe indicar, sabiendo que las mujeres se jubilan con 60 años o más y los hombres con 65 años o más, si la persona está en edad de jubilarse."""

nombre = input("Ingrese su nombre:")
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su genero (F) para mujer o (M) para hombre:")

if edad < 1 or edad > 120:
    print(f"{nombre} la edad estáfuera de rango")
elif genero != "F" and genero != "M":
    print(f"{nombre} Genero inválido")
else:
    if genero == "F" and edad >= 60:
        print(f"{nombre} esta en edad de jubilarse")
    elif genero == "M" and edad >= 65:
        print(f"{nombre} esta en edad de jubilarse")
    else:
        print(f"{nombre} no esta en edad de jubilarse")
