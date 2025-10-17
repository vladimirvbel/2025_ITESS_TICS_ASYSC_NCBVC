"""
    ITESS TICS TI-501
    Análisis de señales y sistemas de comunicaciones
    Docente: Francisco Javier Montecillo Puente
    Estructuras de datos en Python listas por comprensión anidadas
    Programador: Vázquez Coronado Nam_chul Bruno
    17/10/2025
"""

# Definición de una matriz 3x4
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# Transponer la matriz (convertir filas en columnas)
matriz_transpuesta = [[fila[i] for fila in matriz] for i in range(4)]

#Segunda forma de cambiar filas por columnas
transpuesta = []
for i in range(4):
    transpuesta.append([fila[i] for fila in matriz])

#tercera forma de cambiar filas por columnas

transpuesta2 = []
for i in range(4):
    # las siguientes 3 líneas hacen la comprensión de listas anidada
    fila_transpuesta= []
    for fila in matriz:
        fila_transpuesta.append(fila[i])
    transpuesta2.append(fila_transpuesta)



# Mostrar la matriz original y la transpuesta
#---------------------------------------------------------------
print("Matriz original:")
for fila in matriz:
    print(fila)

print("\nMatriz transpuesta:")
for fila in matriz_transpuesta:
    print(fila)

print("\nMatriz transpuesta (segunda forma):")
for fila in transpuesta:
    print(fila)

print("\nMatriz transpuesta (tercera forma)")
for fila in transpuesta2:
    print(fila)
#---------------------------------------------------------------

# la forma más usada es una función predefinida, Función zip()
list(zip(*matriz))  # Convierte filas en columnas
# el asterisco (*) descomprime la lista de listas en argumentos separados
print("\nMatriz transpuesta (usando zip):")
for fila in list(zip(*matriz)):
    print(fila)
