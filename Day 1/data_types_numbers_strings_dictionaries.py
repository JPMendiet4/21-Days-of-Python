"""Tipos de datos: Numbers, Strings y Diccionarios"""

# Números: enteros y flotantes
edad = 25
pi = 3.14159
salario = 1000.50
c = 3e5
millon = 1_000_000

# Las variables pueden ser de cualquier tipo de dato sin embargo existe la opcion de definir el tipo de dato de la variable
edad: int = 25
pi: float = 3.14
salario: float = 1500.50

################################################################################################################################################

# Strings: cadenas de texto
nombre = "Platzi"
apellido = 'Academy'

# Al igual que los números, los strings pueden ser tipados para evitar errores a futuro.
nombre: str = "Platzi"
apellido: str = 'Academy'

# Concatenación de strings
nombre_completo = nombre + " " + apellido
print(nombre_completo) # "Platzi Academy"

# Formateo de strings
nombre_completo = f"{nombre} {apellido}"
print(nombre_completo) # "Platzi Academy"

# Metodos de strings
"""
len(): Devuelve la longitud de un string.
upper(): Devuelve el string en mayúsculas.
lower(): Devuelve el string en minúsculas.
split(): Devuelve una lista de strings separados por un carácter.
"""
################################################################################################################################################

# Diccionarios: colecciones de datos que contienen una clave y un valor.
persona = {
  "nombre": "Fulanita",
  "platziRank": 9567,
	"cursoFavorito": {
		"nombre": "Básico de Python",
		"clases": 30,
		"duracion": "2 horas"
	}
}

# Para acceder a los elementos de un diccionario, podemos utilizar la clave como índice.
print(persona["nombre"]) # "Fulanita"
print(persona["cursoFavorito"]["nombre"]) # "Básico de Python"
print(persona["platziRank"]) # 9567


################################################################################################################################################

# Booleanos: True y False
verdadero = True
falso = False

# Los booleanos son útiles para realizar comparaciones y no pasa nada si olvidas el tipo de dato con el que estas trabajando este siempre se puede recordar con la funcion type()