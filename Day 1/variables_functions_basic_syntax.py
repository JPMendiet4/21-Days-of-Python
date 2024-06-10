"""Variables, funciones y sintaxis básica"""

# Variables: En Python, las variables se definen y se inicializan en una sola línea.
edad = 24
hora = 12

# Funciones: En Python, las funciones se definen con la palabra reservada def y su contenido se define con indentación.
def mi_funcion(parametro1, parametro2):
	# Código de la función
	resultado = parametro1 + parametro2
	return resultado

# Llamar a una función
resultado = mi_funcion(2, 3)
print(resultado)

# Funciones lambda: En Python, las funciones lambda son funciones anónimas que se definen en una sola línea.
saluda = lambda: print("Hola")
saluda()

# "Hola"

################################################################################################################################################

# Sintaxis básica:

# Bloques de código: En Python, los bloques de código se definen con indentación unicamente.
condicion = 2

if condicion % 2 == 0:
    # Código si la condición es verdadera
	print("La condición es verdadera")
else:
    # Código si la condición es falsa
	print("La condición es falsa")
	

# Comentarios: En Python, los comentarios se pueden escribir de dos maneras:

# Comentario de una línea

"""
Comentario de varias lineas
"""