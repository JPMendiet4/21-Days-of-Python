"""Condicionales"""

# if: si la condición es verdadera, se ejecuta el bloque de código

temperature = 15

if (temperature > 20):
    print("es un dia caluroso")
else:
     print("Es un dia frio")

# elif: si la condición anterior no es verdadera, se evalúa la siguiente condición

if (temperature > 10):
     print('El día esta muy frio')
elif (temperature > 20):
     print('El día esta un poc frio')
else:
     print('El clima es calido hoy')


