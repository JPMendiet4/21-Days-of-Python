"""Diccionarios"""

mi_diccionario = {
    'uno': 1,
    'dos': 2,
    'tres': 3
}

curso = {
    'nombre': '30 días de Python',
    'duración': '20 horas',
    'clases': 100,
    'detalles': {
        'tecnologias': ['Python', 'Flask', 'Django'],
        'calificacion': 5,
    },
    'comentarios': ['¡Excelente curso!', 'Python es poderoso', 'Hola']
}

# Acceder a un valor de un diccionario
print(curso['detalles'])
print(curso['detalles']['tecnologias'])

# Diccionarios con metodos
coche = {
    'marca': 'Toyota',
    'encender': lambda: print('El coche ha sido encendido')
}

# llamar un metodo de un diccionario
coche['encender']() # "El coche ha sido encendido"