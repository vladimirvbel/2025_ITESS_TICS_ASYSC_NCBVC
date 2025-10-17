"""
    ITESS TICS TI-501
    Análisis de señales y sistemas de comunicaciones
    Docente: Francisco Javier Montecillo Puente
    Estructuras de datos en Python uso de módulos externos
    Programador: Vázquez Coronado Nam_chul Bruno
    17/10/2025
"""
# ====================================================================
# Uso de un Módulo Externo
# ====================================================================

# 1. Importar el módulo. Esto hace que todo su contenido esté disponible.
import fibo

# 2. Llamar a una función del módulo usando la sintaxis: nombre_modulo.nombre_funcion()
print("--- Llamando a funciones del módulo 'fibo' ---")
print("Llamada a fibo.fib(1000):")
fibo.fib(1000)
print("\nLlamada a fibo.fib2(100):")
print(fibo.fib2(100), "\n")

# 3. Acceder a variables globales del módulo, como __name__
print("--- Atributos del módulo ---")
print("El nombre del módulo es:", fibo.__name__, "\n")


# 4. Asignar una función del módulo a una variable local para un acceso más corto
print("--- Asignar una función a una variable local ---")
fib = fibo.fib # 'fib' ahora apunta a la función fibo.fib
print("Llamada a la función a través de la variable local 'fib(500)':")
fib(500)