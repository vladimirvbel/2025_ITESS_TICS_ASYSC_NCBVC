"""
    ITESS TICS TI-501
    Análisis de señales y sistemas de comunicaciones
    Docente: Francisco Javier Montecillo Puente
    Estructuras de datos en Python sentencias de instrucción 'del'
    Programador: Vázquez Coronado Nam_chul Bruno
    17/10/2025
"""

# Ejemplo de uso de 'del' para eliminar un elemento de una lista por su índice
a = [-1, 1, 66.25, 333, 333, 1234.5]
print("Lista original:", a)
del a[0]

print("Lista modificada:", a)

del a[2:4]
print("Lista después de eliminar elementos en el rango 2:4:", a)
del a[:]
print("Lista después de eliminar todos los elementos:", a)
