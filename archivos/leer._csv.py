import csv

with open("archivos\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)

# cuando vayamos a leer un archivo no es recomendable leerlo con esta libreria si no mejor con pandas