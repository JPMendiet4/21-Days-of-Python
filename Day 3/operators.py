"""Operadores"""

# Operadores aritmeticos

## Suma 
print(1 + 2) # 3

## Resta 
print(1 - 2) # -1

## Multiplicacion
print(1 * 2) # 2

## Division
print(1 / 2) # 0.5

## Division entera
print(3 // 2) # 1

## Modulo (residuo)
print(10 % 3) # 1

## Exponenciacion
print(2 ** 3) # 8

################################################################################################################################################

# Operadores de asignacion

## Asignacion
x = 1

## Suma y asignacion 
x += 2 # x = x + 2

## Resta y asignacion
x -= 1 # x = x - 1

## Multiplicacion y asignacion
x *= 2 # x = x * 2

## Division y asignacion
x /= 2 # x = x / 2

## Division entera y asignacion
x //= 2 # x = x // 2

## Modulo y asignacion
x %= 2 # x = x % 2

## Exponenciacion y asignacion
x **= 2 # x = x ** 2

################################################################################################################################################

# Operadores de comparacion

## Igualdad
print(1 == 1) # True

## Diferencia
print(1 != 1) # False

## Mayor que
print(1 > 1) # False

## Menor que
print(1 < 1) # False

## Mayor o igual que
print(1 >= 1) # True

## Menor o igual que    
print(1 <= 1) # True

## Comparacion
print(1 is '1') # False

################################################################################################################################################


# Operadores logicos

## AND
edad = 22
mayor_de_edad = edad >= 18
if edad >= 18:
    print('Es mayor de edad')
else:
    print('Es menor de edad')

## OR 
tiene_credencial = True

if edad >= 18 or tiene_credencial:
    print('Puede votar')
else:
    print('No puede votar')

## NOT

es_fin_de_seamna = True

if not es_fin_de_seamna:
    print('A trabajar')
else:
    print('Es fin de semana')

