# Día 1

Python es un lenguaje de programación interpretado y multiplataforma que destaca por su sintaxis clara y legible. Es un 
lenguaje multiparadigma, ya que admite programación orientada a objetos, programación imperativa y, en menor medida, 
programación funcional.

Por supuesto, aquí tienes una versión mejorada:

El primer día trabajamos en la sintaxis básica de Python, comenzando con las variables y su declaración, hasta llegar a 
los tipos de datos. A continuación, resumiré parte del contenido:


## Variables, funciones y sintaxis básica

### Variables

Las [variables](https://python.land/courses/python-introduction/lessons/variables) son fundamentales porque permiten asignar nombres a los valores almacenados en memoria. El operador 
de asignación en Python es el `=`, y las variables actúan como referencias a direcciones específicas en memoria.

- Reglas para nombrar variables:

    1. Sólo pueden contener los siguientes tipos de caracteres:
        
        - Letras minúsculas.
        - Letras mayúsculas.
        - Dígitos.
        - Guiones bajos `(_)`.
    
    2. Deben empezar con una letra o un guión bajo, nunca con un dígito.
    3. No pueden ser una palabra reservada del lenguaje (`«keywords»`).

Podemos obtener un listado de las palabras reservadas del lenguaje de la siguiente forma:

```python
>>> help('keywords')

Here is a list of the Python keywords. Enter any keyword to get more help.

False       class           from           or
None        continue        global         pass
True        def             if             raise
and         del             import         return
as          elif            in             try
assert      else            is             while
async       except          lambda         with
await       finally         nonlocal       yield
break       for             not
```

**Nota:** Los nombres de variables son `«case-sensitive»`. Por ejemplo, *stuff* y *Stuff* son nombres diferentes.

```python
age = 24
age2 = 48
last_name = 'Perez Perez'
last_name_2 = 'Perez Perez'
_star = 'Sol'
_3planet = 'Tierra'
```

#### Constantes

Un caso especial de las variables son las constantes, que suelen nombrarse usando letras mayúsculas. Se utilizan para 
indicar variables cuyo valor no cambiará a lo largo del programa.

```python
SOUND_SPEED = 343.2
WATER_DENSITY = 997
EARTH_NAME = 'La Tierra'
```

#### Asignación aumentada

Python nos ofrece la posibilidad de hacer una **asignación aumentada** de la siguiente manera 

```python
tres = three = drei = 3
```
En este caso las tres variables utilizadas en el «lado izquierdo» tomarán el valor 3.

#### Asignando una variable a otra variable

Dada una variable `x` declarada con anterioridad es posible asignarla a una nueva variable `y`

```python
people = 157503
total_population = people
```

#### Conocer el tipo de una variable

Para conocer el tipo de un valor o una variable, Python nos ofrece la función `type()`.

```python
type(24) # <class 'int'>
```

### Funciones

Una [función](https://python.land/introduction-to-python/functions) es una estructura que nos permite agrupar código con dos objetivos claros:

1. No repetir trozos de código durante nuestro programa.
2. Reutilizar el código para distintas situaciones.

Una función se define por su nombre, los parámetros que recibe y el valor que retorna.

#### Definir una función

Para definir una función, utilizamos la palabra reservada `def` seguida del nombre de la función. A continuación, pueden 
aparecer 0 o más parámetros separados por comas dentro de paréntesis, y la línea termina con dos puntos `:`. En la 
siguiente línea comienza el cuerpo de la función, que puede contener una o más sentencias, incluyendo opcionalmente una 
sentencia `return` para devolver un resultado.


```python
def function(parametro1, parametro2):
    # Código de la función
    return resultado
```

#### Invocar una función

Para invocar o "llamar" a una función, simplemente escribimos su nombre seguido de paréntesis. Por ejemplo, para una 
función sencilla (como la vista anteriormente), se haría de la siguiente manera:

```python
function(parametro1, parametro2)
```

### Sintaxis básica 

En Python, al igual que en muchos otros lenguajes de programación, la sintaxis básica permite que las cosas funcionen 
correctamente. A continuación, mostraremos la sintaxis básica para declarar un `if` y para crear comentarios de una y 
varias líneas:

#### Sintaxis para declarar un `if`

```python
if condition:
    # Código si la condición es verdadera
else:
    # Código si la condición es falsa
```

#### Comentarios de una y varias líneas

```python 
# Comentario en una linea 

"""
Comentario 
en 
varias 
lineas
"""
```


## Tipos de datos: Numbers, Strings y Diccionarios

### Números

Los números son de dos tipos principalmente, enteros y flotantes:

- Los números enteros en Python no tienen decimales, pero pueden incluir signo y estar expresados en bases distintas a 
la base 10.

```python
age = 24
salary = 1000
```

- Los números flotantes en Python son aquellos cuyo valor no es exacto y, por lo tanto, requieren el uso del punto (`.`) 
para expresar su parte decimal.

```python
pi = 3.1415
e = 2.718282
```

Si bien también se pueden escribir números complejos en Python, en este caso no los abordaremos. En cambio, veremos que 
a los tipos de datos en Python se les puede añadir tipado, es decir, especificar qué tipo de valor puede recibir una 
variable. Esto asegura que, si se recibe un tipo diferente al declarado, se mostrará un error.

```python
age: int = 24
pi: float = 3.1415926
```

### Strings

Los Strings en Python son secuencias de caracteres, también conocidas como "cadenas de texto". Nos permiten almacenar 
información textual de manera conveniente y versátil.

```python 
name = "Python"
type_of = 'dinamico'
```

- Al igual que con los números, los strings en Python también pueden tener un tipo específico definido: 

```python
name: str = 'Python'
```

- Concatenar strings

```python
type_of_name = name + ' ' + type_of # Python dinamico
```

- Los f-strings son una forma de hacer que el texto sea dinámico en Python, permitiendo la inserción de valores de 
variables directamente en un string de manera sencilla y legible.

```python
full_name = f"El lenguaje de programacion {name} es de tipo {type_of}"
# El lenguaje de programacion Python es de tipo dinamico
```

Algunas otras utilidades de los strings:
- len(): Devuelve la longitud de un string.
- upper(): Devuelve el string en mayúsculas.
- lower(): Devuelve el string en minúsculas.
- split(): Devuelve una lista de strings separados por un carácter.

## Diccionarios 

Los diccionarios son un tipo de dato muy útil en Python porque son ampliamente conocidos en el ámbito de la 
programación, como en JSON. Son estructuras de datos que permiten almacenar información organizada mediante pares de 
`clave : valor`. 

```python 
person = {
  "name": "Fulanita",
  "Rank": 9567,
	"Favorite Course": {
		"name": "Básico de Python",
		"classes": 30,
		"duration": "2 hours"
	}
}
```
- Acceder a los elementos de un diccionario:

```python 
print(person["name"]) # "Fulanita"
print(person["Favorite Course"]["name"]) # "Básico de Python"
print(person["Rank"]) # 9567
```

### Booleanos

Los booleanos son un tipo de dato que puede tener dos valores: `True` o `False`. Son muy útiles para realizar 
comparaciones y tomar decisiones en nuestros programas.

```python
true_value = True
false_value = False
```