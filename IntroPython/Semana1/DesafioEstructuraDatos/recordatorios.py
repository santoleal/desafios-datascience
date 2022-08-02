# Estudiante: Felipe Leal Arancibia
# Desafío de semana 1 - G51
# Fecha: 28/07/2022
 

# Requerimiento 3

# Lista original
recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

#Chequear tipo de datos de variable dada
print(type(recordatorios))

#A pesar de que en el ejemplo "efeméride.py" se sugiere pasar a Diccionario, en este caso se dejará en lista (multilista), ya que no se requiere una clave única (los eventos se pueden superponer, a modo de agenda).

#Chequear primer valor de la multilista, de acuerdo a índices 0
print("\nPrimera lista de la multilista:")
print(recordatorios[0])
print()

#1. Agregue un evento el 2 de Febrero de 2021 a las 6 de la mañana para “Empezar el Año”.
print("\n__________________________")
print("\n1. Agregar evento")
print("__________________________\n")
recordatorios.insert([1][0],['2021-02-02', "06:00", "Empezar el Año"])
# Output resultante
print("\nNueva lista completa con evento añadido:")
print(recordatorios)



#2. Al revisar los eventos, nota un error, ya que el 15 de Julio no es feriado. Editar de tal manera que sea el 16 de Julio.
print("\n__________________________")
print("\n2. Editar evento")
print("__________________________\n")
#Se identifica índide de lista de evento en cuestión
identificar_indice = recordatorios.index(['2021-07-15', "13:00", "No hacer nada es feriado"])
print(f"\nIdentificar índice de evento en cuestión: {identificar_indice}")

#Se lee el evento en cuestión
print(f"Se lee el evento en cuestión: {recordatorios[3]}")

#Se identifica el elemento en la posición exacta
print(f"Esta es la fecha qe se cambiará: {recordatorios[3][0]}")

#Se asigna un nuevo valor a ese índice
recordatorios[3][0] = '2021-07-16'

#Se confirma modificación de índice puntual
print(f"Confirmar fecha cambiada: {recordatorios[3][0]}")

#Se confirma modificación de evento
print(f"Se lee nuevo evento (modificado): {recordatorios[3]}")

# Output final
print("\nNueva lista completa con evento modificado:")
print(recordatorios)



# 3. Lamentablemente le tocará trabajar el día del trabajo. Elimine el evento del día del trabajo.
print("\n__________________________")
print("\n3. Eliminar evento")
print("__________________________\n")
#Identificar índice de lista en cuestión
identificar_indice = recordatorios.index(['2021-05-01', "15:00", "No trabajar"])
print(f"\nIdentificar índice de evento en cuestión: {identificar_indice}")

#Eliminar evento en cuestión a partir de índice identificado
print(f"se eliminará evento: {recordatorios[identificar_indice]}")

del recordatorios[2] 

# Output final
print("\nNueva lista con evento eliminado:")
print(recordatorios)


# 4- Agregue una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a las 22 hrs.
print("\n__________________________")
print("\n4. Agregar nuevos eventos")
print("__________________________\n")
#Se añade en posición 4 la cena de Navidad
print("\nSe añade Cena de Año Nuevo al final de la lista")
recordatorios.insert([4][0], ['2021-12-24', "22:00", "Cena de Navidad"])
# Chequeo de que quedó ok
print(f"Chequeo de Cena de Navidad en índice correspondiente[4]: {recordatorios[4]}")

# Se agrega al final el último evento del año
print("\nSe añade Cena de Año Nuevo al final de la lista")
recordatorios.append(['2021-12-31', "22:00", "Cena de Año Nuevo"])
# Chequeo de que quedó ok
print(f"Chequeo de índice [-1]: {recordatorios[-1]}")




# Output final
print("__________________________")
print("\nLISTA COMPLETA FINAL:")
print("__________________________\n")

print(recordatorios)

print("__________________________")
print("\nDe forma ordenada:")
print("__________________________\n")

for eventos in recordatorios:
    print("Fecha: {:10}  Hora: {:10} Actividad: {:10}".format(eventos[0], eventos[1], eventos[2]))


print("\n__________________________")
print("\nFIN")
print("__________________________\n")

#Gracias! Espero que esté bien el ejercicio. Saludos!
#Felipe Leal Arancibia.