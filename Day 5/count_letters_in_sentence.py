"""
En este desafío deberás implementar la lógica de una función que cuente la cantidad de ocurrencias de cada letra en una cadena de texto y lo almacene en un diccionario.

Es importante mencionar que la función debe ser sensible a mayúsculas y minúsculas, es decir, las letras mayúsculas y minúsculas deben considerarse diferentes.

Ejemplo 1:


Input: "Hola mundo"

Output: {
  'H': 1, 
  'o': 2, 
  'l': 1, 
  'a': 1, 
  ' ': 1, 
  'M': 1, 
  'u': 1, 
  'n': 1, 
  'd': 1
}
"""

def count_letters(phrase):
    # Inicializamos un diccionario vacío
    letters = {}
    # Iteramos sobre cada letra de la frase
    for letter in phrase:
        # Si la letra no está en el diccionario, la inicializamos con 0
        if letter not in letters:
            letters[letter] = 0
        # Incrementamos en 1 la cantidad de ocurrencias de la letra
        letters[letter] += 1
    return letters

# Test
print( count_letters("Hola mundo") ) # {'H': 1, 'o': 2, 'l': 1, 'a': 1, ' ': 1, 'M': 1, 'u': 1, 'n': 1, 'd': 1}
  

count_letters("Hola mundo") # {'H': 1, 'o': 2, 'l': 1, 'a': 1, ' ': 1, 'M': 1, 'u': 1, 'n': 1, 'd': 1}