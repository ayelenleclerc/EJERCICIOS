"""Escribir un programa que permita realizar varias operaciones matemáticas ingresando un caracter por cada una la operación a realizar (‘+’, ‘-’, ‘*’, ‘/’, ‘F’) y dos números enteros en el caso que no haya elegido ‘F’. La computadora debe mostrar el resultado para la operación ingresada. Considerar que no se puede dividir por cero. Cuando la operación ingresada sea ‘F’ nos indicará que no se desean calcular más operaciones.
"""

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

while True:
    operation = input(
        "Ingrese la operación ('+', '-', '*', '/' or 'F' para finalizar): "
    )

    if operation == "F":
        print("Fin del programa.")
        break

    elif operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            result = "No se puede dividir por cero."
        else:
            result = num1 / num2
    else:
        print("Ingrese una operación valida.")
        continue

    print(f"El resultado de la operación {num1}{operation}{num2} es: {result}")
