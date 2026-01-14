# MANERA DE LEER OPTIMA PARA UN ARCHIVO
#with open("archivos\\bloc_notastxt.txt", encoding= "UTF-8") as archivo:
    #print(archivo.read()) # nos trae todo el texto del archivo

    #@print(archivo.readlines(2)) # nos trae el texto de la primera linea 
    
    # no es necesario cerrarlo ya que con el with open ya nos cierra.\


# ------------------- MANERA QUE NO ES TOTALMENTE RECOMENDADBLE---------------
# 1
archivo = open("archivos\\bloc_notastxt.txt", encoding= "UTF-8")


#2.  leer todo el archivo
leer_linea = archivo.read()

# 3. leer linea por linea 
linea_por_linea = archivo.readlines()

#4. cerrar el archivo
archivo.close()

print(leer_linea)

#---------------------ESCRIBIR ARCHIVOS---------------------------------

with open ("archivos\\bloc_notastxt.txt", "w", encoding= "UTF-8") as archivo:
    
    # sobreescribimos es archivo
    archivo.write("hola amigos estoy practicando \n")
    
    # sobreescribimos otra vez el archivo
    archivo.write("hola amigos estoy practicando otra vez \n")
    
    # sobreescribimos el archivo en una sola linea 
    archivo.writelines(["esta es una linea\n" , "Esta es otra linea \n"])

#------------------AGREGAR VARIAS LINEAS DE TEXTO------------------------

with open("archivos\\bloc_notastxt.txt", "a", encoding="UTF-8") as archivo:
    for i in range(5):
        archivo.write(f"Esta es la { i + 1 } linea \n")
