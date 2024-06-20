file = open("archivo.txt", "r")

content = file.read()
print(content)

line = file.readline()
while line:
    print(line)
    line = file.readline()


lines = file.readlines()
for line in lines:
    print(line)


file.close()

try:
    file = open("archivo.txt", "r")
    # Realizar operaciones de lectura
finally:
    file.close()


with open("archivo.txt", "r") as file:
    # Realizar operaciones de lectura


import csv

with open('archivo.csv', 'r') as file:
    # Realizar operaciones de lectura del archivo CSV



with open('archivo.csv', 'r') as file:
    csv_reader = csv.reader(file)
    # Realizar operaciones de lectura del archivo CSV


with open('archivo.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        # Acceder a los valores de cada columna en la fila
        print(row)


with open('archivo.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Acceder a los valores utilizando los nombres de las columnas
        print(row['columna1'], row['columna2'])