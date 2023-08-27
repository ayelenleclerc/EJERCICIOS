"""Para acceder a cierta atracción, alcanza con que se cumpla solamente una de las siguientes condiciones: ser mayor de 6 años o medir más de 1,50 metros.

Escribir un programa en Python que solicite al usuario su edad y estatura, y que determine si cumple con los requisitos para subir a la atracción. Si cumple con al menos una de las condiciones, el programa debe imprimir "¡Puede acceder!" en la pantalla. Si no cumple con ninguna de las condiciones, el programa debe imprimir un mensaje que lo indique.

(Ojo, tener en cuenta las palabras: más, mayor y sobre todo la letra o)

El conector "or" se utiliza para combinar dos o más expresiones lógicas y evaluarlas en conjunto. La expresión completa es verdadera si al menos una de las expresiones individuales es verdadera. Por ejemplo, la expresión lógica "A or B" será verdadera si al menos una de las variables A o B es verdadera. Solo si ambas variables son falsas, entonces la expresión completa será falsa.

La tabla de verdad del "or" es la siguiente:

P	Q	P or Q
V	V	V
V	F	V
F	V	V
F	F	F
El conector "or" se utiliza para crear expresiones lógicas que requieren que al menos una condición sea verdadera para ser verdadera."""

LIMITE_EDAD = 6
LIMITE_ALTURA = 1.50
nombre = input("Ingrese su nombre:")
edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su altura: "))

entra_edad = edad >= LIMITE_EDAD
entra_altura = altura > LIMITE_ALTURA
entra = entra_edad or entra_altura

if entra:
    cartel = "Puedes Acceder!"
else:
    cartel = "No accedes por la altura, ni por la edad"


print(f"Hola {nombre}, {cartel}")
