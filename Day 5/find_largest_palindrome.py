"""
En este desafío, debes crear una función que encuentre el palíndromo más largo en una lista de palabras.

Recibirás un único parámetro: una lista de palabras. Si no hay ningún palíndromo en la lista, la función debe devolver None. Si hay más de un palíndromo con la misma longitud máxima, debes devolver el primer palíndromo encontrado en la lista.

Un palíndromo es una palabra que se puede leer de la misma manera tanto hacia adelante como hacia atrás.

Ejemplo 1:


Input: find_largest_palindrome(["racecar", "level", "world", "hello"])

Output: "racecar"

Ejemplo 2:


Input: find_largest_palindrome(["Platzi", "Python", "django", "flask"])

Output: None
"""

def find_largest_palindrome(words):
    # Inicializamos una variable para almacenar el palíndromo más largo
    largest_palindrome = None
    # Iteramos sobre cada palabra en la lista
    for word in words:
        # Si la palabra es un palíndromo
        if word == word[::-1]:
            # Si no hay ningún palíndromo almacenado, almacenamos el actual
            if largest_palindrome is None:
                largest_palindrome = word
            # Si la longitud del palíndromo actual es mayor a la del almacenado, lo reemplazamos
            elif len(word) > len(largest_palindrome):
                largest_palindrome = word
    return largest_palindrome

# Test
print( find_largest_palindrome(["racecar", "level", "world", "hello"]) ) # "racecar"