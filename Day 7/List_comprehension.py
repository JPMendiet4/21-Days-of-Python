"""List comprehension"""

numeros = [1, 2, 3, 4, 5]

# Crear una nueva lista con el cuadrado de los números pares de la lista original
cuadrados_pares = [num ** 2 for num in numeros if num % 2 == 0]
print(cuadrados_pares)  # Output: [4, 16]

# Crear una nueva lista con los números impares multiplicados por 2 de la lista original
impares_multiplicados = [num * 2 for num in numeros if num % 2 != 0]
print(impares_multiplicados)  # Output: [2, 6, 10]


numeros = [1, 2, 3, 4, 5]

# Crear una nueva lista con los números pares de la lista original, y 'No par' para los impares
numeros_par_o_no_par = ['Par' if num % 2 == 0 else 'No par' for num in numeros]
print(numeros_par_o_no_par)  # Output: ['No par', 'Par', 'No par', 'Par', 'No par']s