"""
    ITESS TICS TI-501
    Análisis de señales y sistemas de comunicaciones
    Docente: Francisco Javier Montecillo Puente
    Estructuras de datos en módulos en Python números Fibonacci
    Programador: Vázquez Coronado Nam_chul Bruno
    17/10/2025
"""
# Módulo de números Fibonacci (fibo.py)

# Función para imprimir la serie de Fibonacci hasta n
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print() # Para un salto de línea final

# Función para devolver la serie de Fibonacci hasta n en una lista
def fib2(n):
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a+b
    return resultado

# --- INICIO DEL NUEVO BLOQUE A AGREGAR ---
# Este código solo se ejecuta si el archivo es llamado directamente
# desde la terminal (ej: python fibo.py 50)
if __name__ == "__main__":
    import sys
    # Llama a la función fib con el argumento pasado desde la terminal
    fib(int(sys.argv[1]))
# --- FIN DEL NUEVO BLOQUE A AGREGAR ---