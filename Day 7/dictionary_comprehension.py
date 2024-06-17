"""Dictionary Comprehension"""

personas = [("Juan", 25), ("María", 30), ("Pedro", 20)]

# Crear un nuevo diccionario con el nombre como clave y la edad como valor, solo para personas mayores de 25 años
personas_mayores = {nombre: edad for nombre, edad in personas if edad > 25}
print(personas_mayores)  # Output: {'María': 30}

# Crear un nuevo diccionario con el nombre como clave y la longitud del nombre como valor para todas las personas
diccionario_longitudes = {nombre: len(nombre) for nombre, _ in personas}
print(diccionario_longitudes)  # Output: {'Juan': 4, 'María': 5, 'Pedro': 5}