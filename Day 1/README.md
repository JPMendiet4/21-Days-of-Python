# Día 1

En el día uno trabajamos todo lo que es la sintaxis básica de Python partiendo desde las variables y como declararlas hasta llegar a los tipos de datos. En este caso voy a resumir un poco del contenido aqui: 

## Variables, funciones y sintaxis básica

### Variables

- Las [variables](https://python.land/courses/python-introduction/lessons/variables) son una herramienta util que sirve para almacenar valores (en realidad son una referencia en memoria a donde se guardo un objeto), generalmente se suelen nombrar usando letras minusculas y evitando usar palabras reservadas del lenguaje, para declarar una varariable se usa el signo de = que funciona como operador de asignacion y se encarga de decirle usted se llama, por ejemplo:

```edad = 24```

- Las [funciones](https://python.land/introduction-to-python/functions) son una herramienta fundamental para todos los leguajes de programacion puesto que permiten crear estructuras de codigo que despues se pueden llamar para hacer una tarea especifica y así ahorrar tiempo, una funcion se declara usando la palabra reservada *def* seguido del nombre de la función, (), : y finalmanete el bloque de codigo identado que se encargara de realizar la tarea:


```python
def function(parametro1, parametro2):
    # Código de la función
    return resultado
```

- Podemos llamar a una función invocandola por su nombre:

```python
resultado = function(a, b)
```

### Sintaxis básica 

En Python al igual que en muchos otros lenguajes de programación hay una estructura que permite que las cosas funcionen bien, esto es lo que se llama sintaxis básica, en este caso vamos a mencionar la sintaxis básica para declara un ```if```, para crear comentarios de una y varias lineas:

- Lo primero que vamos a observar es un bloque de codigo que serai el codigo segido de la declaracion de una función, de un bucle y se define por medio de identacion 

```python
if condicion:
    # Código si la condición es verdadera
else:
    # Código si la condición es falsa
```

- Comentarios, los comentarios son muy importantes dentro del código porque permiten seguir buenas practicas al documentar nuestros proyectos:

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