# Estudiante: Felipe Leal Arancibia
# Fecha: 28/07/2022
# 
""" 1. Crear el programa emprendedor1.py que utilice la fórmula descrita anteriormente
para calcular las utilidades de un proyecto.Para ello utiliza input() para solicitar
como dato el precio de suscripción P, el número de usuarios U y el gasto total GT.
(5 Puntos)
"""

precio_suscripcion = float(input("Ingrese precio de suscripción: \n>"))
numero_usuarios = int(input("Ingrese número de usuarios: \n>"))
gastos_totales = float(input("Ingrese gastos totales: \n>"))

utilidades = precio_suscripcion * numero_usuarios - gastos_totales


print(f"Las utilidades del proyecto de delivery alimento para mascotas es de: {utilidades}")