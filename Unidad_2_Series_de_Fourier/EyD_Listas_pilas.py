"""
    ITESS TICS TI-501
    Análisis de señales y sistemas de comunicaciones
    Docente: Francisco Javier Montecillo Puente
    Estructuras de datos en Python listas como pilas (LIFO)
    Programador: Vázquez Coronado Nam_chul Bruno
    15/10/2025
"""

# 1. Creación de la pila (usando una lista)
print("1. Creación de la Pila")
stack = [3, 4, 5]
print("Pila inicial:", stack, "\n")

# 2. Apilar (push) elementos en la pila. Se usa append() para agregar al final (arriba).
print("2. list.append(x) -> Apilar (Push)")
stack.append(6)
stack.append(7)
print("Pila después de apilar 6 y 7:", stack, "\n")

# 3. Desapilar (pop) elementos de la pila. Se usa pop() para quitar el último elemento.
print("3. list.pop() -> Desapilar (Pop)")

# Primer pop
elemento_quitado = stack.pop()
print("Elemento desapilado:", elemento_quitado)
print("Pila actual:", stack, "\n")

# Segundo pop
elemento_quitado = stack.pop()
print("Elemento desapilado:", elemento_quitado)
print("Pila actual:", stack, "\n")

# Tercer pop
elemento_quitado = stack.pop()
print("Elemento desapilado:", elemento_quitado, "\n")
# Estado final de la pila
print("4. stack")
print("Pila final:", stack, "\n")