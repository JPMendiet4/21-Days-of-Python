# Día 2

En el día dos trabajamos todo lo que son los operadores aritmeticos, asignación aumentada, operadores de comparación y operadores logicos en Python. En este caso voy a resumir un poco del contenido aqui: 

## Operadores aritmeticos 

Los operadoress aritemticos hacen referencia a los elementos usados para poder realizar operaciones básicas entre diferentes valores y/o variables:

- Suma 
```python
1 + 2
```

- Resta
```python
1 - 2
```

- Multiplicación 
```python
1 * 2
```

- División
```python
1 / 2 # 1.5
```

- División entera
```python
3 // 2 # 1 
```

- Modulo (retorna el residuo de la división)
```python
10 % 3 # 1
```

## Asignación aumentada

La asignación aumentada ocurre cuando una vez asignado un valor a una variable se desea realizar una operacion básica siguiendo la estructura `operador=` y esta a su vez se encarga de actualizar de inmediato el valor de la variable

- Asignación
```python
x = 10
```

- Suma
```python 
x += 1 # x + 1
```

- Resta
```python
x -= 1 # x - 1
```

- Multiplicación
```python
x *= 2 # x * 2
```

- División
```python
x /= 4 # x / 4
```

- División entera
```python
x //= 2 # x // 2
```

- Modulo 
```python
x %= 3 # x % 3
```

- Exponenciación
```python
x **= 2 # x ** 2
```

## Operadores de comparación 

Los operadores de comparación son un conjunto de elementos de Python que permiten saber si una variable es diferente o igual a otra gracias a poder compararlas entre si.

- Igualdad
```python
print(1 == 1) # True
```

- Diferencia
```python
print(1 != 1) # False
```

- Mayor que
```python
print(1 > 1) # False
```

- Menor que
```python
print(1 < 1) # False
```

- Mayor o igual que
```python
print(1 >= 1) # True
```

- Menor o igual que    
```python
print(1 <= 1) # True
```

- Comparacion
```python
print(1 is '1') # False
```

## Operadores logicos

Los operadores logicos amplian el campo de trabajo que se logra con los las variables puesto que abren la posibilidad del que pasaria si...

- AND
```python
edad = 22
mayor_de_edad = edad >= 18
if edad >= 18:
    print('Es mayor de edad')
else:
    print('Es menor de edad')
```

- OR 
```python
tiene_credencial = True

if edad >= 18 or tiene_credencial:
    print('Puede votar')
else:
    print('No puede votar')
```

- NOT
```python
es_fin_de_seamna = True

if not es_fin_de_seamna:
    print('A trabajar')
else:
    print('Es fin de semana')
```
    