"""Tuplas"""

mi_tupla = (1, 2)
mi_tupla2 = ((1, 2), (3, 4))
print(mi_tupla2[0])

# como las tuplas son inmutables no se pueden modificar, pero si se puede crear una nueva a partir de otra existente
puntos = ((1, 2), (3, 4), (5, 6))
nuevo_punto = (7, 8)
puntos = puntos[:1] + (nuevo_punto,) + puntos[2:]
print(puntos)

# metodos mas usados en tuplas

# indice de la primera coincidencia
puntos = ((1, 2), (3, 4), (5, 6))
print(puntos.index((3, 4)))

# frecuencia de un elemento 
numeros = (1, 2, 3, 2, 4, 2)
print(numeros.count(2))

# cantidad de elementos en una tupla
puntos = ((1, 2), (3, 4), (5, 6))
print(len(puntos))