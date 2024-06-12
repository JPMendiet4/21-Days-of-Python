# Día 3

En el día dos trabajamos todo lo que son los condicionales y los cilos Python. En este caso voy a resumir un poco del contenido aqui: 

## Condicionales 

Los condicionales se encargan de decirle al leguaje que pasa si se cumple una condición u otra, en este caso hablaremos del `if`

### if

Este condicional le dice al la maquina si se cumple la condición haga esto, sino esto otro, veamos como declarar un `if` en Python

```python
if condicion:
    # codigo si se cumple la condición
else:
    # codigo en caso contrario
```

Si bien es util el tener palabras reservadas como `if` y `else` para hacer validaciones a estas se les agrega una tercera que expande la posibilidad de más de dos comparaciones

```python
if condicion1:
    # codigo si se cumple la condición1
elif condicion2:
   # codigo si se cumple la condición2 
else:
    # codigo en caso contrario
```


## Ciclos

Los ciclos son estrcuturas que se encargan de hacer una tarea repetitiva meintras se cumpla una condición

### For

El ciclo `for` le indica a la maquina que para un elemento dentro de otro que se pueda recorrer como una lista, un rango o un string haga una accion

```python 
for elemento en secuencia:
    #codigo que se ejecuta
```

### While

El ciclo `while` le indica a la maquina que mientras algo se cumpla puede haga una tarea

```python 
while condicion:
    #codigo que se ejecuta
```

A  la hora de usar ciclos es importante estar atentos para no caer en bucles infinitos como puede sucerder con `while True` el cual siempre va a ser verdad por lo que nunca va a parar de ejecutarse el codigo