# Estudiante: Felipe Leal Arancibia
# Desafío de semana 1 - G51
# Fecha: 28/07/2022
 

# Requerimiento 2
import re #Utilizada para limpiar el texto de caracteres no pertinentes para este ejercicio
from collections import Counter  #Esta es para jugar un poco con la frecuencia de palabras

print("__________________________")
print("\nINICIO DE EJERCICIO")
print("__________________________\n")

with open("Apoyo_Desafío_Estructura_datos/lorem_ipsum.txt", "r") as file:
    texto=file.read()

#caracteres_distintos = int(input())
#palabras_distintas = int(input())

#Lectura del texto importado
print("Se imprime texto orginal, para chequear que está bien importado:\n")
print(texto)
print(" ")

#Chequear tipo de datos del texto 
print("Se chequea el tipo de dato del archivo importado:")
print(type(texto))
print(" ")
#print(dir(texto))

#Conteo de caracteres y palabras distintas del texto original
print("________________________________________________________\n")
print("PRIMER CONTEO DE CARACTERES Y PALABRAS: TEXTO ORIGINAL")
print("________________________________________________________")
print(f"Número de caracteres totales del texto original: {len(texto)}")
print(f"Número de palabras totales del texto original: {len(texto.split())}\n\n")

#Limpieza de texto original, sin "." ni ","... Con ello se crea un nuevo texto (nueva variable newtexto)
newtexto = re.sub('[,.]','',texto)

#También se aprovecha de pasar el texto nuevo a minúscula, para evitar cualquier problema de repetición de palabras por case sensitive
newtexto = newtexto.lower()
print(f"\n\nAhora, así queda Lorem Ipsum sin puntos ni comas, y en minúscula. Esto es parte de la limpieza de los datos para un trabajo más preciso: \n\n{newtexto}\n\n")


#Ahora se separan las palabras distintas por espacio en blanco. Con ello se crea una lista

print(f"\n\nLista de palabras separadas de texto limpio Lorem Ipsum.txt (en bruto, varias se repiten): \n\n{newtexto.split()}\n\n")



#Conteo de caracteres y palabras distintas del nuevo texto depurado
#Conteo de caracteres y palabras distintas del texto original
print("________________________________________________________\n")
print("SEGUNDO CONTEO DE CARACTERES Y PALABRAS: NUEVO TEXTO DEPURADO")
print("________________________________________________________")
print(f"\n\nEl número de caracteres totales del nuevo texto depurado es: {len(newtexto)}")
print(f"El número de palabras totales del nuevo texto depurado es: {len(newtexto.split())}\n\n")


#Ahora, ordenar alfabéticamente la lista del texto nuevo para ver -al ojo- si hay repeticiones o no 
palabras_distintas = newtexto.split()
palabras_distintas.sort()
print(f"\nAhora, se ordena la lista por orden alfabético para visualizar posibles repeticiones: \n\n{palabras_distintas}\n\n")

# Como se ve, hay repeticiones. Por ello, ahora se procede a convertir lista a set para agrupar y generar lista-conjunto por palabras únicas
palabras_unicas = set(palabras_distintas)

#Se vueve a ordenar alfabéticamente la lista de palabras únicas
print(f"\nDado que hay repeticiones, se procede a ordenar por agrupación de palabras, para así generar listado de palabras únicas:\n\n{sorted(palabras_unicas)}\n\n")

#Conteo de palabras distintas de acuerdo a agrupación SET 
print("________________________________________________________\n")
print("TERCER CONTEO DE (SÓLO) PALABRAS: AGRUPACIÓN SET")
print("________________________________________________________")
print(f"Número de palabras únicas -distintas- del nuevo set (texto limpio): {len(palabras_unicas)}\n\n")

#Ahora, con la librería Counter, procederemos a generar un listado que indique cuántas veces se repite cada palabra. Por defecto se crea como diccionario; se puede pasar a lista, pero lo dejaremos así nomás.
frecuencia_palabras = Counter(palabras_distintas)
print(f"\nAhora, por experimentar, se visualiza la frecuencia de palabras de acuerdo al texto limpio:\n\n{frecuencia_palabras}\n")


#Final: Resumen comparativo de conteo de palabras: 
print("___________________________________________\n")
print("RESUMEN DE EJERCICIO DE CONTEO DE PALABRAS")
print("___________________________________________")
#Conteo de caracteres y palabras distintas del texto original
print(f"\n\nNúmero de caracteres totales del texto original: {len(texto)}")
print(f"Número de palabras totales del texto original: {len(texto.split())}")
print(f"Número de caracteres totales del nuevo texto depurado: {len(newtexto)}")
print(f"Número de palabras totales del nuevo texto depurado: {len(palabras_distintas)}")
print(f"Número de palabras únicas -distintas- del nuevo set (texto limpio): {len(palabras_unicas)}\n\n")


print("\n__________________________")
print("\nFIN")
print("__________________________\n")

#Gracias! Espero que esté bien el ejercicio. Saludos!
#Felipe Leal Arancibia.