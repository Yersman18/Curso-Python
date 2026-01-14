with open("archivos\\bloc_notastxt.txt", 'a', encoding="UTF-8") as archivo:
    # agregando el archivo
    for i in range(5):
        archivo.writelines([f'linea {i + 1 } \n'])

# writelines: nos funciona cuando queremos agregar varias lineas
# write : nos funciona para escribir en una solo linea


