"""
Escribir un programa de python que permita validar la nota de un examen. Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.
La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.
Las notas 1 y 3 no usan nunca.
La nota 0 se reserva para los ausentes.
Las notas válidas pueden ser un 2 o un valor entre 4 y 10.
No usar funciones
"""
while True:
    nota = input("Ingrese la nota del examen o F para finalizar: ").upper()
    if nota == "F":
        print("Fin del programa.")
        break
    nota = int(nota)
    if nota == 0:
        print("Nota válida: Ausente.")
    elif nota == 1 or nota == 3:
        print("Nota inválida: No se utiliza.")
    elif 2 <= nota <= 10:
        print("Nota válida.")
    else:
        print("Nota inválida. Debe ser un 2 o un valor entre 4 y 10.")
        print("Ingrese un valor numérico válido o 'F' para finalizar.")
