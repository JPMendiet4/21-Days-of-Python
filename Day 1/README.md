# Día 1

Python es un lenguaje de programación interpretado y multiplataforma cuya filosofía hace hincapié en una sintaxis que 
favorezca el código legible, se trata de un lenguaje de programación multiparadigma, ya que soporta orientación a 
objetos, programación imperativa y, en menor medida, programación funcional.

En el día uno trabajamos todo lo que es la sintaxis básica de Python partiendo desde las variables y como declararlas 
hasta llegar a los tipos de datos. En este caso voy a resumir un poco del contenido aqui: 


## Variables, funciones y sintaxis básica

### Variables

Las [variables](https://python.land/courses/python-introduction/lessons/variables) son fundamentales ya que permiten definir nombres para los valores almacenados en memoria (son una 
referencia a una dirección en memoria).

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

**Nota:** Los nombres de variables son `«case-sensitive»`. Por ejemplo, *stuff* y *Stuff*
son nombres diferentes.

```python
age = 24
age2 = 48
last_name = 'Perez Perez'
last_name_2 = 'Perez Perez'
_star = 'Sol'
_3planet = 'Tierra'
```

#### Constantes

Un caso especial de las variables son las constantes las cuales se suelen nombrar usando letras mayúsculas y se usan 
para indicar variables cuyo valor no va a cambiar a lo largo de nuestro programa

```python
SOUND_SPEED = 343.2
WATER_DENSITY = 997
EARTH_NAME = 'La Tierra'
```

#### Asignación múltiple

Python nos ofrece la posibilidad de hacer una **asignación múltiple** de la siguiente manera 

```python
tres = three = drei = 3
```
En este caso las tres variables utilizadas en el «lado izquierdo» tomarán el valor 3.

#### Asignando una variable a otra variable

Dada una variable `x` definida previamente se puede asignar a una nueva variable `y`

```python
people = 157503
total_population = people
```

#### Conocer el tipo de una variable

Para conocer el tipo de un valor o una variable, Python nos ofrece la función `type()`.

### Funciones

Una [función](https://python.land/introduction-to-python/functions) una estructura que nos permite agrupar código y perseguir dos objetivos claros:
1. No repetir trozos de código durante nuestro programa.
2. Reutilizar el código para distintas situaciones.

Una función viene definida por su nombre, sus parámetros y su valor de retorno.

#### Definir una función

Para definir una función utilizamos la palabra reservada `def` seguida del nombre de la función. A continuación 
aparecerán 0 o más parámetros separados por comas (entre  paréntesis), finalizando la línea con dos puntos : En la 
siguiente línea empezaría el cuerpo  de la función que puede contener 1 o más sentencias, incluyendo (o no) una 
sentencia de  retorno con el resultado mediante return.


```python
def function(parametro1, parametro2):
    # Código de la función
    return resultado
```

#### Invocar una función

Para invocar (o «llamar») a una función sólo tendremos que escribir su nombre seguido de
paréntesis. En el caso de la función sencilla (vista anteriormente) se haría así:

```python
resultado = function(a, b)
```

### Sintaxis básica 

En Python al igual que en muchos otros lenguajes de programación hay una estructura que permite que las cosas funcionen 
bien, esto es lo que se llama sintaxis básica, en este caso vamos a mencionar la sintaxis básica para declara un 
```if```, para crear comentarios de una y varias lineas:

- Lo primero que vamos a observar es un bloque de codigo que serai el codigo segido de la declaracion de una función, 
- de un bucle y se define por medio de identacion 

```python
if condicion:
    # Código si la condición es verdadera
else:
    # Código si la condición es falsa
```

- Comentarios, los comentarios son muy importantes dentro del código porque permiten seguir buenas practicas al 
- documentar nuestros proyectos:

```python 
# Comentario de una linea 
"""
Comentario 
de 
varias 
lineas
"""
```


## Tipos de datos: Numbers, Strings y Diccionarios

Una vez conocido un poco de las variables y la sintaxis básica de python es hora de hablar de los tipos de datos que se pueden almacenar en una variable.

### Números

Los números como todos los conocesmos son de dos tipos principalmente, enteros y racionales o decimales que en este caso se llman float

- Los numeros enteros son aquellos que se expresan de manera combencional sin necesidad de usar puntos ni nada para expresarlos:

```python
edad = 24
salario = 1000
```

- Los números de tipo float son aquellos cuyo valor no es exacto y en consecuencia debe usarse el **.** para expresar su parte decimal:

```python
pi = 3.1415
e = 2.71
```

Si bien tambien se pueden escribir los números complejos en este caso no lo vamoa a abordar, por el contario vamos a ver que a los tipos de datos en Python se les puede agregar tipado, es decir que tipo de valor puede recibe una variable lo cual generara que en caso de resivir un tipo diferente al declarado se muestre un error:

```python
edad: int = 24
pi: float = 3.1415926
```

### Strings

Los strings son las cadenas de caracteres y se pueden declarar usando "" o '' y todo lo que este dentro de estas comillas sera interpretado como texto:

```python 
nombre = "Python"
tipo = 'Dinamico'
```

- Al igual que se hizo con los numeros los strings tambien se pueden tipar: 

```python
nombre: string = 'Platzi'
```

- Concatenar strings

```python
nombre_tipo = nombre + ' ' + tipo
# Python dinamico
```

- F strings son una forma de poder hacer que el texto sea dinamico permitindo que se ingresen valores de variables a un string

```python
nombre_completo = f"El lenguaje de programacion {nombre} es de tipo {tipo}"
# El lenguaje de programacion Python es de tipo dinamico
```

Algunas otras utilidades de los strings:
- len(): Devuelve la longitud de un string.
- upper(): Devuelve el string en mayúsculas.
- lower(): Devuelve el string en minúsculas.
- split(): Devuelve una lista de strings separados por un carácter.

## Diccionarios 

Los diccionarios son un tipo de dato muy util porque son ampliamente conocidos en el ambito de la programación como JSON y son estructuras de datos que permiten almacenar informacion siguiendo la estructura de clave : valor 

```python 
persona = {
  "nombre": "Fulanita",
  "platziRank": 9567,
	"cursoFavorito": {
		"nombre": "Básico de Python",
		"clases": 30,
		"duracion": "2 horas"
	}
}
```
- Acceder a los elementos de un diccionario:

```python 
print(persona["nombre"]) # "Fulanita"
print(persona["cursoFavorito"]["nombre"]) # "Básico de Python"
print(persona["platziRank"]) # 9567
```

### Booleanos

Este tipo de datos solo incluye dos opciones, True y False que son de vital importancia dentro de las validaciones, comprobaciones y el sofware en general

```python
verdadero = True
falso = False
```

***Bonus:** podemos saber el tipo de dato de una variable usando la funcion ```type```

**Regla general:**

- Usar nombres para variables (ejemplo article).
- Usar verbos para funciones (ejemplo get_article()).
- Usar adjetivos para booleanos (ejemplo available).