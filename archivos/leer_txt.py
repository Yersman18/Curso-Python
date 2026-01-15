# archivo = open("archivos\\bloc_notastxt.txt", endcoding = "UTF-8" )
# print(archivo.read())

# Otra manera de imprimmir el resultadode una variable
archivo = open("archivos\\bloc_notastxt.txt", encoding = "UTF-8" )

# leer archivo completo
#archivo_sin_leer = archivo.read()

# leer linea por linea
#lineas = archivo.readlines() 

# leer una sola linea 
linea = archivo.readline() # readline(200) por caracteres


#cerrar el archivo
#archivo.close()


# despues de cerrarlo ya no podemos hacer uso sobre el archivo
#print(archivo.read())





