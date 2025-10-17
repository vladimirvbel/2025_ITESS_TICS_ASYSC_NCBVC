"""
    ITESS TICS TI-501
    Análisis de señales y sistemas de comunicaciones
    Docente: Francisco Javier Montecillo Puente
    Estructuras de datos en Python diccionarios
    Programador: Vázquez Coronado Nam_chul Bruno
    17/10/2025
"""

# ====================================================================
# EJEMPLO 1: Operaciones básicas con Diccionarios
# Un diccionario almacena pares de clave:valor no ordenados.
# ====================================================================

# 1. Creación de un diccionario
print("--- 1. Creación del diccionario ---")
tel = {'jack': 4098, 'sape': 4139}
print("Diccionario inicial:", tel, "\n")

# 2. Agregar un nuevo par clave:valor
print("--- 2. Agregar un elemento ---")
tel['guido'] = 4127
print("Diccionario después de agregar a 'guido':", tel, "\n")

# 3. Acceder al valor de una clave
print("--- 3. Acceder a un valor por su clave ---")
print("El número de 'jack' es:", tel['jack'], "\n")

# 4. Eliminar un par clave:valor
print("--- 4. Eliminar un elemento y agregar otro ---")
del tel['sape']
tel['irv'] = 4127
print("Diccionario después de eliminar a 'sape' y agregar a 'irv':", tel, "\n")

# 5. Obtener una lista de todas las claves
print("--- 5. Obtener las claves ---")
# La función list() convierte las claves en una lista
print("Lista de claves (orden arbitrario):", list(tel.keys()))
# La función sorted() devuelve las claves en orden alfabético
print("Lista de claves (ordenadas):", sorted(tel.keys()), "\n")

# 6. Verificar la existencia de una clave con 'in' y 'not in'
print("--- 6. Verificar si una clave existe ---")
print("¿Está 'guido' en el diccionario?", 'guido' in tel)
print("¿No está 'jack' en el diccionario?", 'jack' not in tel)

# ====================================================================
# Formas alternativas de crear Diccionarios
# ====================================================================

# 1. Usando el constructor dict() con una lista de tuplas (clave, valor)
print("--- 1. Creación con dict() y tuplas ---")
diccionario_tuplas = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(diccionario_tuplas, "\n")

# 2. Usando comprensión de diccionarios
#    Sintaxis: {clave_expresión: valor_expresión for variable in iterable}
print("--- 2. Creación con comprensión de diccionarios ---")
diccionario_comprension = {x: x**2 for x in (2, 4, 6)}
print(diccionario_comprension, "\n")

# 3. Usando dict() con argumentos de palabra clave (solo para claves de tipo string)
print("--- 3. Creación con dict() y palabras clave ---")
diccionario_kwargs = dict(sape=4139, guido=4127, jack=4098) # keyword arguments
print(diccionario_kwargs)

# ====================================================================
# Técnicas de Iteración (Looping)
# ====================================================================

# 1. Iterar sobre un diccionario con .items() para obtener clave y valor
print("--- 1. Iterar sobre un diccionario (clave y valor) ---")
caballeros = {'gallahad': 'el puro', 'robin': 'el valiente'}
for k, v in caballeros.items():
    print(k, v)
print("\n")


# 2. Iterar sobre una secuencia con enumerate() para obtener índice y valor
print("--- 2. Iterar con índice y valor ---")
for i, v in enumerate(['ta', 'te', 'ti']):
    print(i, v)
print("\n")


# 3. Iterar sobre dos o más secuencias a la vez con zip()
print("--- 3. Iterar sobre dos secuencias en paralelo ---")
preguntas = ['nombre', 'objetivo', 'color favorito']
respuestas = ['lancelot', 'el santo grial', 'azul']
for p, r in zip(preguntas, respuestas):
    print('Cual es tu {0}? {1}.'.format(p, r))
print("\n")


# 4. Iterar sobre una secuencia en orden inverso con reversed()
print("--- 4. Iterar en orden inverso ---")
for i in reversed(range(1, 10, 2)):
    print(i)
print("\n")


# 5. Iterar sobre una secuencia ordenada y sin duplicados con sorted(set())
print("--- 5. Iterar en orden sobre elementos únicos ---")
canasta = ['manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana']
# set(canasta) crea una colección con elementos únicos: {'naranja', 'pera', 'banana', 'manzana'}
# sorted() ordena esa colección alfabéticamente
for f in sorted(set(canasta)):
    print(f)
print("\n")


# 6. Modificar una lista mientras se itera sobre ella (usando una copia)
print("--- 6. Modificar una lista mientras se itera ---")
palabras = ['gato', 'ventana', 'defenestrar']
# Usamos palabras[:] para crear una copia superficial de la lista sobre la que iterar.
# Esto evita comportamientos inesperados al modificar la lista original.
for p in palabras[:]:
    if len(p) > 6:
        palabras.insert(0, p)
print("Lista final modificada:", palabras)