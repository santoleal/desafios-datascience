# Estudiante: Felipe Leal Arancibia
# Fecha: 28/07/2022
"""
Requerimientos
1. Se solicita crear un script escape.py que permita calcular la velocidad de escape
ingresando como datos de entradas el radio r y la constante g. Los datos de entrada
deben ingresarse de manera interactiva utilizando la función input().
(5 Puntos)
2. El programa debe especificar claramente el formato en el que se deben entregar los
datos de entrada con instrucciones apropiadas.
(5 Puntos)
Ej:
“Ingrese el radio en Kilómetros:”,
“Ingrese la constante g: ”
La respuesta del programa también debe mostrarse con un texto apropiado:
Ej:
“La velocidad de Escape es 11174.6 [m/s]”
● Para verificar el correcto funcionamiento del programa, se puede verificar con
los siguientes datos:
○ g = 9.8 [m/s2]
○ r = 6371 [Km]
● Se obtiene como resultado:
○ Velocidad de Escape = 11174.6 [m/s]

"""

import math


# Requerimiento 1 y Requerimiento 2

constante_gravitacional = float(input("Ingrese la constante gravitacional (en metros/segundos2): \n"))
radio_km = float(input("Ingrese el radio del planeta (en kilómetros): \n"))

# conversión kilómetros a metros 
radio_planeta = radio_km * 1000

# Fórmula principal
velocidad_escape = math.sqrt (2 * (constante_gravitacional * radio_planeta )) 

print(f"La velocidad de escape del planeta es: {velocidad_escape:.2f} m/s.")

