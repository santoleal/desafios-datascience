#almacenar diferentes fechas importantes
#este va a ser con Diccionario

efemerides = {'1 de enero': 'Año nuevo',
            '27 de febrero': 'Terremoto en Chile',
            '8 de marzo': 'Día de la Mujer',
            '18 de septiembre': 'Fiestas Patrias',
            '25 de diciembre': 'Navidad'}

fecha = input("Ingresa una fecha \n").lower()

print(f'Efemérides: {efemerides.get(fecha, "No hay evento para esta fecha")}')
