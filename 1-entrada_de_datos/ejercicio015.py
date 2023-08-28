"""Definición del problema: Una inmobiliaria paga a sus vendedores un salario base, más una comisión fija por cada venta realizada, más el 5% del valor de esas ventas. Realizar un programa que imprima el nombre del vendedor y el salario que le corresponde en un determinado mes.

Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.

¿Sobran datos? ¿Qué datos sobran?

"""
vendedor = input("Ingrese el nombre del vendedor: ")
salario_fijo = float(input("Ingrese el salario fijo del vendedor: "))
ventas = float(input("Ingrese la cantidad de ventas realizadas: "))
comision_fija = float(input("Ingrese la comisión fija: "))
comision_variable = 0.5 * ventas
salario_total = salario_fijo + comision_fija + comision_variable

print(f"El salario total del vendedor {vendedor} es de ${salario_total}")
