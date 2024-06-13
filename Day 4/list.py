"""Listas"""

# Crear una lista 
mi_lista = [1, 2, 2, 2, 3]
print(mi_lista)

#Modificar un elemnto de una lista
mi_lista[1] = -2
print(mi_lista)

# Agregar un elemento a una lista 
mi_lista.append('4')
print(mi_lista)

# Eliminar un elemanto de la una lista
mi_lista.pop(3)
print(mi_lista, 'aqui')

# Cuantas veces esta un elemento en una lista
print(mi_lista.count(2))

# Extender una lisat con otra
mi2_lista = [4, 5, 6, 7, 8]
mi_lista.extend(mi2_lista)
print(mi_lista)

# Invertir el orden de los elementos de una lista
mi2_lista.reverse()
print(mi2_lista)

# Ordenar una lista
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]
numeros.sort()
print(f'{numeros= }')

numeros.sort(reverse=True)
print(f'{numeros= }') 