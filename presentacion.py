"""
#Ejercicio guiado con consecha propia

nombre = input("Ingrese su nombre: \n>")
edad = int(input("Ingrese su edad: \n>"))
ocupacion = input("Ingrese su ocupación: \n>")
lugar_trabajo = input("Ingrese su lugar de trabajo: \n>")
pasatiempos = input("Ingrese su pasatiempo: \n>")
gustaria_hacer =  input("Ingrese lo que le gustaría hacer en el futuro próximo: \n>")

print(f"¡Hola! Mi nombre es {nombre}. Tengo {edad} años. Soy {ocupacion}, y trabajo en {lugar_trabajo}. En mis momentos libres, tengo como pasatiempos lo siguiente: {pasatiempos}. En el futuro cercano, me encantaría: {gustaria_hacer}. Eso. Muchas gracias, pewkayeal!")
"""

#Mismo ejercicio pero con sys.argv, que permite ingresar valores en la lista de acuerdo al orden del índice, argumentos desde la terminal de fomra directa, a diferencia de input, que pregunta todo.

import sys

nombre = sys.argv[1]
edad =  sys.argv[2]
ocupacion =  sys.argv[3]
lugar_trabajo =  sys.argv[4]
pasatiempos =  sys.argv[5]
gustaria_hacer =   sys.argv[6]

print(f"¡Hola! Mi nombre es {nombre}. Tengo {edad} años. Soy {ocupacion}, y trabajo en {lugar_trabajo}. En mis momentos libres, tengo como pasatiempos lo siguiente: {pasatiempos}. En el futuro cercano, me encantaría: {gustaria_hacer}. Eso. Muchas gracias, pewkayeal!")
 
print(type(sys.argv))

# ¿Esto se puede asociar a una base de datos que ya cuenta con estas columnas ordenadas, como por ejemplo, las de los email personalizados?
