# Estudiante: Felipe Leal Arancibia
# Fecha: 28/07/2022
# 
""" 3. Considera ahora una tercera versión llamada emprendedor3.py utilizando la fórmula
original de utilidades donde el usuario ingrese el precio de suscripción P, el número
de usuarios normales U y los gastos GT. Adicionalmente, solicita las utilidades del
año anterior Uanterior, todo esto mediante input(). El programa debe calcular las
utilidades actuales y mostrar la razón entre las utilidades actuales y las del año
anterior con dos decimales.
(2 Puntos)
"""

import math

print("Advertencia: Ingrese sólo números")

precio_suscripcion = float(input("Ingrese precio de suscripción: \n>"))
numero_usuariosnormales = int(input("Ingrese número de usuarios normales: \n>"))
gastos_totales = float(input("Ingrese gastos totales: \n>"))

utilidades_anioanterior = float(input("Ingrese utilidades del año anterior: \n>"))


utilidades = precio_suscripcion * numero_usuariosnormales - gastos_totales

comparacion_utilidades = utilidades / utilidades_anioanterior

print(f"Las utilidades actuales del proyecto son de {utilidades}. La razón entre las utilidad actual  y la del año anterior ({utilidades_anioanterior}) es de: {comparacion_utilidades:.2f}.")
