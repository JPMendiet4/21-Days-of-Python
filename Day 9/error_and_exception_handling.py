try:
    # Código sospechoso
except ExceptionType:
    # Manejar la excepción

try:
    # Código sospechoso
except ValueError:
    # Manejar la excepción ValueError
except:
    # Manejar cualquier otra excepción

try:
    # Código sospechoso 
except ExceptionType:
    # Manejar la excepción 
finally:
    # Código que se ejecuta siempre

if condition:
    raise ExceptionType("Mensaje de error")


raise TypeError("Se esperaba un tipo de dato diferente")

try:
    # Código sospechoso
except ExceptionType:
    # Manejar la excepción
else:
    # Código que se ejecuta si no hay excepciones

try:
    # Código sospechoso
except ValueError as ve:
    # Manejar excepción ValueError
except TypeError as te:
    # Manejar excepción TypeError