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

# Asignación multiple
tres = three = drei = 3

# Asignando una variable a otra variable
people = 157503
total_population = people

# Conocer el valor de una variable
print(age)

# Conocer el tipo de una variable
print(type(age))

# Conocer la dirección de memoria de una variable
print(id(age))


########################################################################################################################

# Funciones:

# Una función que no recibe parámetros
def say_hello():
	print('Hola!')


# Invocar una función
say_hello()


# Retornar un valor
def one():
	return 1


one()


# Función con un parámetro
def truthiness(obj):
	if obj:
		print(f'{obj} es verdadero')
	else:
		print(f'{obj} es falso')


truthiness(False)
truthiness(0)
truthiness(None)
truthiness('')
truthiness([])
truthiness({})
truthiness(())
truthiness(0.0)
truthiness(set())

truthiness(True)
truthiness(1e-10)
truthiness([0])
truthiness(('', ))
truthiness(' ')


# Función con dos parámetros
def _min(a, b):
	if a < b:
		return a
	else:
		return b


_min(7, 9)


# Una función con argumentos posicionales
def build_cpu(vendor, num_cores, freq):
	return {
		'vendor': vendor,
		'num_cores': num_cores,
		'freq': freq
	}


build_cpu('AMD', 8, 2.7)
build_cpu(8, 2.7, 'AMD')

# Argumentos nominales
build_cpu(vendor='AMD', num_cores=8, freq=2.7)
build_cpu(num_cores=8, freq=2.7, vendor='AMD')


# Parámetros por defecto
def build_cpu(vendor, num_cores, freq=3.0):
	return {
		'vendor': vendor,
		'num_cores': num_cores,
		'freq': freq
	}


build_cpu('INTEL', 2)
build_cpu('INTEL', 2, 3.4)


# Datos mutables como parametro

def buggy(arg, result=[]):
	result.append(arg)
	print(result)


buggy('a', [])
buggy('b', [])
buggy('a', ['x', 'y', 'z'])
buggy('b', ['x', 'y', 'z'])

buggy('a')
buggy('b')


# Solución 1
def works(arg):
	result = []
	result.append(arg)
	print(result)


works('a')
works('b')


# Solución 2
def nonbuggy(arg, result=None):
	if result is None:
		result = []
	result.append(arg)
	print(result)


works('a')
works('b')
nonbuggy('a', ['x', 'y', 'z'])
nonbuggy('a', ['x', 'y', 'z'])
# Funciones lambda:
greet = lambda: print("Hola")
#greet()

########################################################################################################################

# Sintaxis básica:

# Bloques de código:
condition = 2

"""if condition % 2 == 0:
	print("Es par")
else:
	print("No es par")"""


if __name__ == '__main__':
	print('entro')
	one()
	_min(7, 9)
	build_cpu('AMD', 8, 2.7)