"""
    ITESS TICS TI-501
    Análisis de señales y sistemas de comunicaciones
    Docente: Francisco Javier Montecillo Puente
    Estructuras de datos en Python listas como colas (FIFO)
    Programador: Vázquez Coronado Nam_chul Bruno
    15/10/2025
"""

# Se necesita importar el objeto 'deque' del módulo 'collections'
from collections import deque

# 1. Creación de la cola (usando deque)
print("1. Creación de la Cola")
queue = deque(["Eric", "John", "Michael"])
print("Cola inicial:", queue, "\n")

# 2. Encolar (enqueue) elementos. Se usa append() para agregar al final.
print("2. deque.append(x) -> Enqueue")
queue.append("Terry")   # Terry se forma al final de la fila
queue.append("Graham")  # Graham se forma detrás de Terry
print("Cola después de que llegan Terry y Graham:", queue, "\n")

# 3. Desencolar (dequeue) elementos. Se usa popleft() para quitar al primero que llegó.
print("3. deque.popleft() -> Dequeue")

# El primero en la fila (Eric) se va
primero_en_salir = queue.popleft()
print("Se fue de la cola:", primero_en_salir)
print("Cola actual:", queue, "\n")

# El siguiente en la fila (John) se va
segundo_en_salir = queue.popleft()
print("Se fue de la cola:", segundo_en_salir)
print("Cola final (los que quedan esperando):", queue, "\n")