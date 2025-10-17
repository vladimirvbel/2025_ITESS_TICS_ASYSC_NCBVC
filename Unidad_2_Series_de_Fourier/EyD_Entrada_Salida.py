"""
    ITESS TICS TI-501
    Análisis de señales y sistemas de comunicaciones
    Docente: Francisco Javier Montecillo Puente
    Estructuras de datos en Python formateo de salida y manejo de archivos
    Programador: Vázquez Coronado Nam_chul Bruno
    17/10/2025
"""
# ====================================================================
# Parte 1: Formateo Elegante de la Salida
# ====================================================================

# --- Diferencia entre str() y repr() ---
print("--- 1. str() vs repr() ---")
s = 'Hola mundo.'
# str() es para una visualización legible
print("str(s):", str(s))
# repr() es para una representación que Python pueda interpretar (agrega comillas)
print("repr(s):", repr(s))
print("str(1/7):", str(1/7))

x = 10 * 3.25
y = 200 * 200
# El repr() de una tupla
print("repr de una tupla:", repr((x, y, ('carne', 'huevos'))), "\n")


# --- Creación de Tablas con Alineación ---
print("--- 2. Formateo de tablas ---")
# Método 1: Usando repr(), rjust() y print()
print("Método con rjust():")
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))
print()

# Método 2: Usando el método str.format() (más moderno y preferido)
print("Método con str.format():")
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
print("\n")


# --- Métodos de Relleno y Formato ---
print("--- 3. Relleno y formateo básico ---")
# .zfill() rellena con ceros a la izquierda
print("'12'.zfill(5) ->", '12'.zfill(5))
print("'-3.14'.zfill(7) ->", '-3.14'.zfill(7))

# Uso básico de .format()
print("\nUso básico de format():")
print('Somos los {} quienes decimos "{}!"'.format('caballeros', 'Nop'))

# Usando índices posicionales
print('{0} y {1}'.format('carne', 'huevos'))
print('{1} y {0}'.format('carne', 'huevos'))

# Usando argumentos nombrados (keyword arguments)
print('Esta {comida} es {adjetivo}.'.format(comida='carne', adjetivo='espantosa'))

# Combinando argumentos posicionales y nombrados
print('La historia de {0}, {1}, y {otro}.'.format('Bill', 'Manfred', otro='Georg'), "\n")


# --- Formato Avanzado ---
print("--- 4. Formato avanzado con format() ---")
import math
# Usando !r para aplicar repr() dentro de format()
print('Pi con formato normal: {}.'.format(math.pi))
print('Pi con formato !r: {!r}.'.format(math.pi))

# Redondeando a un número específico de decimales
print('Pi redondeado a 3 decimales: {0:.3f}.'.format(math.pi), "\n")

# Formateando una tabla con anchos de columna fijos
print("Tabla de teléfonos:")
tabla = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for nombre, telefono in tabla.items():
    print('{0:10} ==> {1:10d}'.format(nombre, telefono))
print()

# Usando un diccionario para poblar la cadena de formato
tabla = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# Accediendo por clave
print('Acceso por clave: Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(tabla))
# Usando ** para desempaquetar el diccionario como argumentos nombrados
print('Acceso con **: Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**tabla), "\n")


# --- Viejo Formateo de Cadenas (con %) ---
print("--- 5. Viejo estilo de formato con % ---")
# Aunque funcional, se prefiere .format() o f-strings en código nuevo
print('El valor de PI es aproximadamente %5.3f.' % math.pi, "\n\n")



# ====================================================================
# Parte 2: Leyendo y Escribiendo Archivos
# ====================================================================

# --- Escribiendo en un Archivo ---
print("--- 6. Escribiendo en un archivo ---")
# 'w' es para escribir (write). Si el archivo existe, lo sobreescribe.
f = open('archivodetrabajo', 'w')
print("Objeto archivo creado:", f)

# .write() escribe una cadena en el archivo
num_chars_escritos = f.write('Esto es una prueba\n')
print("Caracteres escritos:", num_chars_escritos)

# Para escribir otros tipos de datos, primero se convierten a string
valor = ('la respuesta', 42)
s = str(valor)
f.write(s)
f.close() # Es importante cerrar el archivo para guardar los cambios.
print("Archivo 'archivodetrabajo' ha sido escrito y cerrado.\n")


# --- Leyendo desde un Archivo ---
print("--- 7. Leyendo desde un archivo ---")
# Abrimos el archivo de nuevo, esta vez en modo lectura ('r'), que es el modo por defecto.
f = open('archivodetrabajo')

# .read() lee el contenido completo del archivo
contenido_completo = f.read()
print("Contenido leído con f.read():")
print(repr(contenido_completo))

# Si intentas leer de nuevo, no hay nada más que leer
print("Segunda llamada a f.read():", repr(f.read()))
f.close()

# Iterar sobre las líneas de un archivo (método recomendado y eficiente)
print("\nIterando sobre las líneas del archivo:")
for linea in open('archivodetrabajo'):
    print(linea, end='')
print("\n")


# --- Moviéndose en el Archivo con seek() y tell() ---
print("--- 8. Moviéndose dentro del archivo (seek y tell) ---")
# 'rb+' abre el archivo para leer y escribir en modo binario
f = open('archivodetrabajo', 'rb+')

# Escribimos una secuencia de bytes
f.write(b'0123456789abcdef')

# .seek(offset, from_where) mueve el cursor. from_where=0 es el inicio.
f.seek(5) # Va al 6to byte
print("Posición actual:", f.tell())
print("Leyendo 1 byte en la posición 5:", f.read(1))

# from_where=2 es el final del archivo. Usamos offset negativo para ir hacia atrás.
f.seek(-3, 2) # Va al 3er byte antes del final
print("Posición actual:", f.tell())
print("Leyendo 1 byte en esa posición:", f.read(1))
f.close()