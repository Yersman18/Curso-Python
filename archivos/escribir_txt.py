with open("archivos\\bloc_notastxt.txt", 'w', encoding="UTF-8") as archivo:
    # sobreescribiendo el archivo 
    #archivo.writelines(["Sobreescribiendo el archivo \n"])

    # agregando otras 2 lineas
    archivo.writelines(["Estamos agregando texto escrbiendo de lo que sea para probar que nos funciona \n", "Esta es otra linea \n"])

    # agregando otras 2 lineas
    archivo.writelines(["Estamos agregando texto escrbiendo de lo que sea para probar que nos funciona \n", "Esta es otra linea"])

