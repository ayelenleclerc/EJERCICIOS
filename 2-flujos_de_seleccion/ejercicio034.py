"""Escribir un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es casado se le incrementa el sueldo en 7% del salario bruto por cada año de antigüedad. También se le realizan los siguientes descuentos:
Jubilación: 11%
Obra Social: 3%
Sindicato: 3%
Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y estado civil (S: Soltero / C: Casado). Se debe informar: (reemplazando los 9 por los valores que correspondan)
Estado Civil: Soltero/Casado Sueldo básico: $ 999.99 Antigüedad: 99 años
Descuentos:
Jubilación - 999,99
Obra Social - 999,99
Sindicato - 999,99
Sueldo Neto 999,99

"""
sueldo_basico = float(input("Sueldo basico:"))
antiguedad = int(input("Antiguedad:"))
estado_civil = input("Estado civil (S: Soltero / C: Casado):")

JUBILACION = sueldo_basico * 0.11
OBRA_SOCIAL = sueldo_basico * 0.03
SINDICATO = sueldo_basico * 0.03

DESCUENTOS = JUBILACION + OBRA_SOCIAL + SINDICATO

SUELDO_SOLTERO = sueldo_basico * 0.05
SUELDO_CASADO = sueldo_basico * 0.07

SOLTERO_ANTIGUEDAD = SUELDO_SOLTERO * antiguedad
CASADO_ANTIGUEDAD = SUELDO_CASADO * antiguedad

SUELDO_NETO_SOLTERO = sueldo_basico + SOLTERO_ANTIGUEDAD - DESCUENTOS

SUELDO_NETO_CASADO = sueldo_basico + CASADO_ANTIGUEDAD - DESCUENTOS

if estado_civil == "S":
    print(f"Sueldo Neto: ${SUELDO_NETO_SOLTERO:,.2f}")
elif estado_civil == "C":
    print(f"Sueldo Neto: ${SUELDO_NETO_CASADO:,.2f}")
else:
    print("Estado civil no valido")
