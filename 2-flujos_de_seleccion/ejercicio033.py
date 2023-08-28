"""La farmacia Sindical efectúa descuentos a sus afiliados según el importe de la compra con la siguiente escala:

Menor de $5500.0 el descuento es del 4.5%
Entre $5500.0 y $10000.0 el descuento es del 8%
Más de $10000.0 el descuento es del 10.5%
Escribir un programa que reciba un importe e informe: el descuento y el precio neto a cobrar, con mensajes aclaratorios.

"""

DESCUENTO1 = 4.5 / 100
DESCUENTO2 = 8 / 100
DESCUENTO3 = 10.5 / 100

importe = float(input("Ingrese el importe: "))

if importe < 5500:
    descuento = importe * DESCUENTO1
    precio = importe - descuento
    print(f"El descuento es ${descuento} (4.5%) y el precio neto a cobrar es {precio}")
elif importe >= 5500 and importe < 10000:
    descuento = importe * DESCUENTO2
    precio = importe - descuento
    print(f"El descuento es ${descuento} (8%) y el precio neto a cobrar es {precio}")
else:
    descuento = importe * DESCUENTO3
    precio = importe - descuento
    print(f"El descuento es ${descuento} (10.5%) y el precio neto a cobrar es {precio}")
