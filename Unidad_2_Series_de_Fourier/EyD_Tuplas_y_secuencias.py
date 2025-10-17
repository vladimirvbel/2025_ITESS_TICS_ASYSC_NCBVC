"""
    ITESS TICS TI-501
    Análisis de señales y sistemas de comunicaciones
    Docente: Francisco Javier Montecillo Puente
    Estructuras de datos en Python tuplas y secuencias
    Programador: Vázquez Coronado Nam_chul Bruno
    17/10/2025
"""

# Tipo de dato secuencia: Tuplas y Secuencias
# ================================================
# La tupla consiste un número de valores separados por comas
t = 12345, 54321, '¡hola!'

print(t[0]) # Imprime el primer elemento de la tupla
print(t)    # Imprime toda la tupla
# Las tuplas son inmutables, no se pueden modificar
# Las tuplas pueden anidarse:
u = t, (1, 2, 3, 4, 5)
print(u)

# Las tuplas son inmutables:
## t[0] = 88888  # Esto generará un error
# Pero pueden contener objetos mutables:
v = ([1, 2, 3], [3, 2, 1])
print(v)

# Tupla 
vacio = ()
singleton = 'hola',  # La coma es necesaria
print("Longitud de la tupla vacía:", len(vacio))
print("Longitud de la tupla singleton:", len(singleton))

singleton

""" la declaración t = 12345, 54321, '¡hola!' es un ejemplo de
    tuplas: los valores 12345, 54321 y '¡hola!' se empaquetan
    juntos en una sola tupla.
"""
# operación inversa - desempaquetado de secuencias
x, y, z = t
print(x, y, z)