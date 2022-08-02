# Estudiante: Felipe Leal Arancibia
# Desafío de semana 1 - G51
# Fecha: 28/07/2022
 

# Requerimiento 1
import sys

# Todo el ejercicio se ejecutará desde la consola con los valores asignados a incorporar de forma directa: 0.0046 0.093 0.0013 10000

print("__________________________")
print("\nINICIO DE EJERCICIO")
print("__________________________\n")

# chequear ruta para trabajar desde terminal
print(sys.argv[0])

sol_peruano = float(sys.argv[1])
peso_argentino = float(sys.argv[2])
dolar_americano = float(sys.argv[3])
peso_chileno = float(sys.argv[4])

print(f"Los ${peso_chileno}.- pesos chilenos equivalen a: ")
print(f"${sol_peruano * peso_chileno}.- Soles Peruanos")
print(f"${peso_argentino * peso_chileno}.- Pesos Argentinos")
print(f"${dolar_americano * peso_chileno}.- Dólares Americanos") 
        

print("\n__________________________")
print("\nFIN")
print("__________________________\n")

#Gracias! Espero que esté bien el ejercicio. Saludos!
#Felipe Leal Arancibia.