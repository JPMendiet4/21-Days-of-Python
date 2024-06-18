def aplicar_operacion(func, a, b):
	return func(a, b)

def suma(a, b):
	return a + b

def resta(a, b):
	return a - b

resultado = aplicar_operacion(suma, 5, 3)
print(resultado)  # Output: 8

resultado = aplicar_operacion(resta, 10, 7)
print(resultado)  # Output: 3