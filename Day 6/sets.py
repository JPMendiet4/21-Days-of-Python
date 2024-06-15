"""Sets """

# Crear un set
my_set = {1, 2, 3, 4, 5}

# Crear un set a partir de una lista
my_list = [1, 2, 3, 4, 5, 5, 5, 5, 5]
my_set = set(my_list)


my_set = set()

# Agregar elementos al set
my_set.add(1)
my_set.add(2)
my_set.add(3)

# Imprimir el set
print(my_set)  # Output: {1, 2, 3}

# Verificar si un elemento existe en el set
print(2 in my_set)  # Output: True

# Eliminar un elemento del set
my_set.remove(2)

# Verificar si un elemento existe en el set después de ser eliminado
print(2 in my_set)  # Output: False

# Vaciar el set
my_set.clear()

# Verificar el tamaño del set después de ser vaciado
print(len(my_set))  # Output: 0

my_set = {1, 2, 3, 4, 5}

# Iterar sobre los elementos del set
for element in my_set:
    print(element)


my_set = {1, 2, 3, 4, 5}

# Iterar sobre los elementos del set a partir del segundo elemento
for item in my_set[1:]:
    print(item)


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Usando el método intersection()
intersection = set1.intersection(set2)
print(intersection)  # Output: {4, 5}

# Usando el operador &
intersection = set1 & set2
print(intersection)  # Output: {4, 5}