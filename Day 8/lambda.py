# Ejemplo 1: Función lambda simple
suma = lambda a, b: a + b
resultado = suma(2, 3)
print(resultado)  # Output: 5

# Ejemplo 2: Uso de lambda con map()
numeros = [1, 2, 3, 4, 5]
duplicados = list(map(lambda x: x * 2, numeros))
print(duplicados)  # Output: [2, 4, 6, 8, 10]

# Ejemplo 3: Uso de lambda con filter()
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Output: [2, 4]
