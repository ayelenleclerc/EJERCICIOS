"""Crear un programa que pida un número de mes (ejemplo 4) y escriba el nombre del mes en letras ("abril"). Verificar que el mes sea válido e informar en caso que no lo sea.

"""
mes = int(input("Ingrese el numero del mes: "))
if mes == 1:
    cartel = "Enero"
elif mes == 2:
    cartel = "Febrero"
elif mes == 3:
    cartel = "Marzo"
elif mes == 4:
    cartel = "Abril"
elif mes == 5:
    cartel = "Mayo"
elif mes == 6:
    cartel = "Junio"
elif mes == 7:
    cartel = "Julio"
elif mes == 8:
    cartel = "Agosto"
elif mes == 9:
    cartel = "Septiembre"
elif mes == 10:
    cartel = "Octubre"
elif mes == 11:
    cartel = "Noviembre"
elif mes == 12:
    cartel = "Diciembre"
else:
    cartel = "Mes no valido"
print(cartel)
