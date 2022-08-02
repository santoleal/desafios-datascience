# Grado alcohólico en alimentos

"""
#ESTA ES LA PRIMERA FORMA QUE REALICÉ. EL SIMPLE + EN EL IMPUT ME ARROJA TYPE ERROR POR CONCATENAR INT A STR, POR LO QUE SE DEBE PASAR A ALGUNO DE LOS MÉTODOS DE CONCATENACIÓN. EN ESTE CASO: (f"...{}...{}..."). REVISAR OTROS MÉTODOS EN: https://www.askpython.com/python/string/python-concatenate-string-and-int
#  

alcohol_alimento = int(input("Indique el grado alcohólico del alimento: ")) 
calorias = int(alcohol_alimento * 7)

print(f"El grado alcohólico de este alimento es de {alcohol_alimento} grados, por lo que el total de calorías es de {calorias} calorias" )

"""

# ESTA ES LA RESPUESTA DE ADL. OJO CON QUE HUBO UNA "INVESTIGACIÓN" PREVIA SOBRE "CALORÍAS"

#importar librería math
import math

#solicitud de imputs. Aquí se especifican las cuatro formas de obtener calorías. No lo dio el ejercicio textual, se tuvo que averiguar. 
proteina = float(input("Ingrese los gr de proteína del alimento:\n>")) 
carbohidratos = float(input("Ingrese los gr de carbohidrato:\n>"))
grasa = float(input("Ingrese los gr de grasa:\n>"))
alcohol =  float(input("Ingrese el grado alcohólico:\n>"))

#cálculo de calorías
calorias = 4 * (proteina + carbohidratos) + 9 * (grasa) + 7 * (alcohol)

#output solicitado
print(f'De acuerdo con los datos entregados, las calorías aportadas son: {math.ceil(calorias)}')

#ojo que la librería math, ne su función ceil, rendondea al entero más próximo mayor que x.
