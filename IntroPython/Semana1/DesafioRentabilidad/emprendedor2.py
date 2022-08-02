# Estudiante: Felipe Leal Arancibia
# Fecha: 28/07/2022
# 

""" 2. Supongamos ahora que el emprendedor considera 2 tipos de usuarios diferenciados,
los usuarios normales y los usuarios premium a los cuales se les cobrará una
suscripción un 50% mayor. Crea una segunda versión llamada emprendedor2.py que
permita considerar el caso recién expuesto. Para ello modifica la fórmula de
utilidades en la cual se solicite mediante input() los parámetros de entrada precios
de suscripción P, así como el número de usuarios Unormal y Upremium y el gasto total GT.
(3 Puntos)
"""



precio_suscripcion = float(input("Ingrese precio de suscripción: \n>"))
numero_usuariosnormales = int(input("Ingrese número de usuarios normales: \n>"))
numero_usuariospremium = int(input("Ingrese número de usuarios premium: \n>"))
gastos_totales = float(input("Ingrese gastos totales: \n>"))

utilidades = precio_suscripcion * (numero_usuariosnormales) + (numero_usuariospremium * (precio_suscripcion + precio_suscripcion * 0.5)) - gastos_totales


print(f"Las utilidades del proyecto son de {utilidades}, considerando que existen usuarios normales ({numero_usuariosnormales}) y usuarios premium ({numero_usuariospremium}).")

