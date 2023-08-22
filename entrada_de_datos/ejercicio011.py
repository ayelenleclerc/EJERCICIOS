"""Escribir un programa que permita resolver el siguiente problema:

Tres personas aportan diferente capital a una sociedad y desean saber el valor total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje).

Solicitar la carga por teclado del nombre de cada socio y su capital aportado, a partir de esto calcular e informar lo requerido previamente."""


persona1 = input("Ingrese el nombre de la persona 1:")
inversion1 = float(input(f"Ingrese la cantidad invertida por {persona1} :"))

persona2 = input("Ingrese el nombre de la persona 2:")
inversion2 = float(input(f"Ingrese la cantidad invertida por  {persona2} :"))

persona3 = input("Ingrese el nombre de la persona 3:")
inversion3 = float(input(f"Ingrese la cantidad invertida por  {persona3} :"))

total = inversion1 + inversion2 + inversion3

porcentaje1 = inversion1 / total * 100
porcentaje2 = inversion2 / total * 100
porcentaje3 = inversion3 / total * 100

print(
    f"""
El total es de ${total}
El porcentaje de {persona1} es de %{porcentaje1:.2f}
El porcentaje de {persona2} es de %{porcentaje2:.2f}
EL porcentaje de {persona3} es de %{porcentaje3:.2f}
"""
)
