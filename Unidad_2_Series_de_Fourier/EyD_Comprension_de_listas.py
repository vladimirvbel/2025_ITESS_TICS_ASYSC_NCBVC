"""
    ITESS TICS TI-501
    Análisis de señales y sistemas de comunicaciones
    Docente: Francisco Javier Montecillo Puente
    Estructuras de datos en Python comprensión de listas
    Programador: Vázquez Coronado Nam_chul Bruno
    15/10/2025
"""

# ====================================================================
# EJEMPLO 1: Crear una lista con los cuadrados de los números del 0 al 9
# ====================================================================

# Forma Tradicional (usando un bucle for)
print("--- Ejemplo 1: Cuadrados (Forma Tradicional) ---")
cuadrados_tradicional = []
for x in range(10):
  cuadrados_tradicional.append(x**2)
print("Lista de cuadrados:", cuadrados_tradicional, "\n")


# Forma con Comprensión de Listas (más concisa)
print("--- Ejemplo 1: Cuadrados (con Comprensión de Listas) ---")
cuadrados_comprension = [x**2 for x in range(10)]
print("Lista de cuadrados:", cuadrados_comprension, "\n\n")



# ====================================================================
# EJEMPLO 2: Combinar elementos de dos listas si no son iguales
# ====================================================================

# Forma Tradicional (con bucles anidados y un if)
print("--- Ejemplo 2: Combinaciones (Forma Tradicional) ---")
combs_tradicional = []
for x in [1, 2, 3]:
  for y in [3, 1, 4]:
    if x != y:
      combs_tradicional.append((x, y))
print("Lista de combinaciones:", combs_tradicional, "\n")


# Forma con Comprensión de Listas
print("--- Ejemplo 2: Combinaciones (con Comprensión de Listas) ---")
combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print("Lista de combinaciones:", combs, "\n")

# ====================================================================
# EJEMPLO 3: Aplicar operaciones a cada elemento de una lista
# ====================================================================
vec = [-4, -2, 0, 2, 4]
print("--- Lista original 'vec' ---")
print(vec, "\n")

# 3.a) Crear una nueva lista con los valores duplicados
print("--- Duplicar cada elemento ---")
duplicados = [x * 2 for x in vec]
print("Lista con valores duplicados:", duplicados, "\n")

# 3.b) Filtrar la lista para excluir números negativos
print("--- Filtrar números negativos ---")
positivos = [x for x in vec if x >= 0]
print("Lista solo con no-negativos:", positivos, "\n")

# 3.c) Aplicar una función (abs) a todos los elementos
print("--- Aplicar la función abs() ---")
absolutos = [abs(x) for x in vec]
print("Lista con valores absolutos:", absolutos, "\n")


# ====================================================================
# EJEMPLO 4: Llamar a un método en cada elemento
# ====================================================================
frutafresca = [' banana', ' mora de Logan ', 'maracuya ']
print("--- Lista original 'frutafresca' con espacios ---")
print(frutafresca, "\n")

# 4.a) Quitar espacios en blanco de cada cadena
print("--- Llamar al método .strip() ---")
limpia = [arma.strip() for arma in frutafresca]
print("Lista sin espacios en blanco:", limpia, "\n")


# ====================================================================
# EJEMPLO 5: Crear una lista de tuplas (pares de valores)
# ====================================================================

# 5.a) Crear una lista de tuplas (número, número al cuadrado)
#      Nota: La expresión (x, x**2) debe estar entre paréntesis.
print("--- Crear una lista de tuplas (número, cuadrado) ---")
tuplas_cuadrados = [(x, x**2) for x in range(6)]
print("Lista de tuplas:", tuplas_cuadrados, "\n")


# ====================================================================
# EJEMPLO 6: Aplanar una lista (convertir lista de listas en una sola)
# ====================================================================
vec_anidada = [[1,2,3], [4,5,6], [7,8,9]]
print("--- Lista anidada original ---")
print(vec_anidada, "\n")

# 6.a) Aplanar la lista con una comprensión de listas y dos 'for'
print("--- Aplanar la lista ---")
plana = [num for elem in vec_anidada for num in elem]
print("Lista aplanada:", plana, "\n")


# ====================================================================
# EJEMPLO 7: Comprensiones con expresiones complejas
# ====================================================================
from math import pi

# 7.a) Crear una lista de strings con PI redondeado a diferentes decimales
print("--- Expresiones complejas (redondear PI) ---")
pi_redondeado = [str(round(pi, i)) for i in range(1, 6)]
print("Lista de PI redondeado:", pi_redondeado, "\n")