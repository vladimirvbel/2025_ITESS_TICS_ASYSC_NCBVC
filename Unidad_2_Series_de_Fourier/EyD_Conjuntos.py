"""
    ITESS TICS TI-501
    Análisis de señales y sistemas de comunicaciones
    Docente: Francisco Javier Montecillo Puente
    Estructuras de datos en Python conjuntos
    Programador: Vázquez Coronado Nam_chul Bruno
    17/10/2025
"""

canasta = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana'}
print (canasta)                   # muestra que se removieron los duplicados
# {'pera', 'manzana', 'banana', 'naranja'}
print('naranja' in canasta)         # verificación de pertenencia rápida
# True
print('yerba' in canasta)
# False
# veamos las operaciones para las letras únicas de dos palabras

a = set('abracadabra')
b = set('alacazam')
a                                  # letras únicas en a
# {a', 'r', 'b', 'c', 'd'}
print(a - b)                              # letras en a pero no en b
# {'r', 'b', 'd'}
print(a | b)                              # letras en a o en b
# {'a', 'c', 'b', 'd', 'm', 'l', 'r', 'z'}
print(a & b)                              # letras en a y en b
# {'a', 'c'}
print(a ^ b)                              # letras en a o b pero no en ambos
# {'b', 'd', 'm', 'l', 'r', 'z'}

# =========================================
# Comprensión de conjuntos: 

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)