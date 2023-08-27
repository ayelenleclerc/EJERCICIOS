"""Existen dos reglas que identifican dos conjuntos de valores:

a) El número es de un solo dígito.
b) El número es impar.
A partir de estas reglas, escribir un programa que permita ingresar un número entero.

Debe asignar el valor que corresponda a las variables booleanas:

esDeUnSoloDigito
esImpar
estaEnAmbos
noEstaEnNinguno
el valor Verdadero o Falso, según corresponda, para indicar si el valor número ingresado pertenece o no a cada conjunto. Definir un lote de prueba de varios números y probr el algoritmo, escribiendo los resultados.

"""

numero = int(input("Ingrese un numero: "))

tiene_un_solo_digito = numero >= 0 and numero <= 9
es_impar = (numero % 2) == 1
esta_en_ambos = tiene_un_solo_digito and es_impar
no_esta_en_ninguno = not esta_en_ambos

print(
    f"""
El numero {numero} tiene un solo digito: {tiene_un_solo_digito}
El numero {numero} es impar: {es_impar}
El numero {numero} esta en ambos: {esta_en_ambos}
El numero {numero} no esta en ninguno: {no_esta_en_ninguno}"""
)
