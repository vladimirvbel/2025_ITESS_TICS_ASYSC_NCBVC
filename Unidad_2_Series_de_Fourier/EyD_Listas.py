"""
    ITESS TICS TI-501
    Análisis de señales y sistemas de comunicaciones
    Docente: Francisco Javier Montecillo Puente
    Estructuras de datos en Python listas
    Programador: Vázquez Coronado Nam_chul Bruno
    15/10/2025
"""

# 1 Crear una lista
print("1. Creación de la lista")
a = [66.25, 333, 333, 1, 1234.5]
print("Lista a: ", a, "\n")

# 2 Devuelve el número de veces que x aparece en la lista.
print("2. list.count(x)")
print("Devuelve el conteo de elementos en la lista (333,66.25,'x'): ", a.count(333), a.count(66.25), a.count('x'), "\n")

# 3 Inserta un elemento en una posición dada y después agrega un elemento al final.
print("3. list.insert(i, x) y list.append(x)")
a.insert(2, -1) # Inserta -1 en la posición 2
a.append(333) # Agrega 333 al final de la lista
print("Lista después de insertar -1 en la posición 2 y agregar 333 al final: ", a, "\n")

# 4 Devuelve el índice de la primera aparición de un elemento.
#    Nota: Si el elemento no se encuentra, generará un error.
print("4. list.index(x)")
print("Índice de la primera aparición de 333:", a.index(333), "\n")

# 5 Elimina la primera aparición de un elemento de la lista.
print("5. list.remove(x)")
a.remove(333) # Busca y elimina el primer 333
print("Lista después de eliminar la primera aparición de 333:", a, "\n")

# 6 Invierte el orden de los elementos en la lista.
print("6. list.reverse()")
a.reverse()
print("Lista después de invertir su orden:", a, "\n")

# 7 Ordena los elementos de la lista de menor a mayor.
print("7. list.sort()")
a.sort()
print("Lista después de ordenarla:", a, "\n")

# 8 Elimina el último elemento de la lista y lo devuelve.
print("8. list.pop()")
elemento_eliminado = a.pop()
print("Elemento eliminado del final:", elemento_eliminado)
print("Lista final después de usar pop():", a, "\n")