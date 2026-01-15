# ## manera recomendable de leer un archivo
# with open("archivos\\bloc_notastxt.txt", encoding= "UTF-8") as archivo:
#     #print(archivo.read())

#     # todo en una sola linea 
#     print(archivo.readlines())

# SOBRE ESCRIBIR EL ARCHIVO 

with open("archivos\\bloc_notastxt.txt", 'w', encoding="UTF-8") as archivo:
    print(archivo.write("Estamos sobreescribiendo el archivo para la practica \n"))
    print(archivo.write("Estamos sobreescribiendo el archivo para la practica \n"))
    print(archivo.writelines(['Esto es un una linea\n', 'y esta es otra linea']))