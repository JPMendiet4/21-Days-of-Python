"""Variables, funciones y sintaxis básica"""

# Variables
age = 24
age2 = 48
last_name = 'Perez Perez'
last_name_2 = 'Perez Perez'
_star = 'Sol'
_3planet = 'Tierra'

# Constantes
SOUND_SPEED = 343.2
WATER_DENSITY = 997
EARTH_NAME = 'La Tierra'

########################################################################################################################

# Funciones:
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