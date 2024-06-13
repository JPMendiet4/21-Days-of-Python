# Día 4

En el día dos trabajamos todo lo que son las listas, diccionarios y tuplas, a continuacion un pequeño resumen

## Listas

Las listas son una estructura de datos fundamental mutable, es decir que se puede modificar su contenido y sigue siendo el mismo objeto, por otro lado las listas permiten almacenar más de un elemento 

```python
mi_lista = [valor1, valor2, valor3]
```

Las listas al ser tipos de datos mutables tienen mciertos metodos y utilidades que permiten hacer grandes cosas tales como:

- Modificar un elemnto de una lista

```python
mi_lista = [valor1, valor2, valor3]
mi_lista[1] = valor # [valor1, valor, valor3]
```

- Agregar un elemento a una lista 

```python
mi_lista = [valor1, valor2, valor3]
mi_lista.append(valor4)
# [valor1, valor2, valor3, valor4]
```
- Eliminar un elemento de una lista

```python
mi_lista = [valor1, valor2, valor3, valor4]
mi_lista.pop()
# [valor1, valor2, valor3, 4]
```
- Saber cuantas veces esta un elemento en una lista

```python
mi_lista.count(valor)
```
- Extender una lista con otra

```python
mi_lista = [valor1, valor2]
mi_lista2 = [valor3, valor4]
mi_lista.extend(mi2_lista) # [valor1, valor2, valor3, valor4]
```
- Invertir el orden de los elementos de una lista

```python
mi_lista.reverse()
```
- Ordenar una lista

```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]
numeros.sort() # [1, 1, 2, 3, 4, 5, 5, 6, 9]

numeros.sort(reverse=True) # [9, 6, 5, 5, 4, 3, 2, 1, 1]
```

## Diccionarios

AL igual que las listas los diccionarios son estructuras de datos que permiten almacenar varios valores sigueindo la estructura de clave valor y al ser mutables son muy dinamicos en cuanto a los valores que se le pueden dar a una clave, veamos unas posibilidades:

- Diccionario estandar, el más básico

```python
mi_diccionario = {
    clave1: valor1,
    clave2: valor2,
    clave3: valor3
}
```
- Diccionario con listas como valor

```python
curso = {
    'nombre': '30 días de Python',
    'duración': '20 horas',
    'clases': 100,
    'detalles': {
        'tecnologias': ['Python', 'Flask', 'Django'],
        'calificacion': 5,
    },
    'comentarios': ['¡Excelente curso!', 'Python es poderoso', 'Hola']
}
```

- Acceder a un valor de un diccionario

```python
curso['detalles']
curso['detalles']['tecnologias']
```
- Diccionarios con metodos (funcion lambda)

```python
coche = {
    'marca': 'Toyota',
    'encender': lambda: print('El coche ha sido encendido')
}
```

- llamar un metodo de un diccionario

```python
coche['encender']() # "El coche ha sido encendido"
```

# Tuplas

Las tuplas son estructuras de datos inmutables por lo que no se puede hacer cambios y de modificar una tupla existente se crea un nuevo objeto con una direccion en memoria diferente, veamos algunas funcionalidades de las tuplas

- Declarar una tupla

```python
mi_tupla = (1, 2)
mi_tupla2 = ((1, 2), (3, 4))
```

- Crear una nueva a partir de una tupla existente

```python
puntos = ((1, 2), (3, 4), (5, 6))
nuevo_punto = (7, 8)
puntos = puntos[:1] + (nuevo_punto,) + puntos[2:]
```

- Indice de la primera coincidencia

```python
puntos = ((1, 2), (3, 4), (5, 6))
puntos.index((3, 4))
```

- Frecuencia de un elemento 

```python
numeros = (1, 2, 3, 2, 4, 2)
numeros.count(2)
```

- Cantidad de elementos en una tupla

```python
puntos = ((1, 2), (3, 4), (5, 6))
len(puntos)
```