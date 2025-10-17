"""
    ITESS TICS TI-501
    Análisis de señales y sistemas de comunicaciones
    Docente: Francisco Javier Montecillo Puente
    Estructuras de datos en Python formas de importar y explorar módulos
    Programador: Vázquez Coronado Nam_chul Bruno
    17/10/2025
"""
# ====================================================================
# Formas de importar y explorar módulos
# ====================================================================

# 1. Importar nombres específicos directamente con 'from ... import ...'
print("--- 1. Importando nombres específicos ---")
from fibo import fib # Importa solo la función 'fib'
fib(500) # Se puede llamar directamente, sin 'fibo.'
print("\n")


# 2. Importar todos los nombres con '*' (no recomendado en scripts)
print("--- 2. Importando todo con '*' ---")
from fibo import *
fib(500)
print("\n")


# 3. La función dir() para ver el contenido de los módulos
import fibo, sys
print("--- 3. Usando dir() para explorar módulos ---")
# Muestra los nombres definidos dentro del módulo 'fibo'
print("Contenido de 'fibo':", dir(fibo))
print("\n")


# 4. dir() sin argumentos para ver los nombres en el espacio actual
print("--- 4. Usando dir() para el espacio actual ---")
a = [1, 2, 3, 4, 5]
# Muestra todo lo que hemos definido o importado hasta ahora
print("Nombres definidos actualmente:", dir())