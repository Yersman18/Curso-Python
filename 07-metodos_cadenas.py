cadena1 = "Hola bien venido a Este curso"

mayuss = cadena1.upper()

minus = cadena1.lower()

PriMayu = cadena1.capitalize()

buscar = cadena1.find("Hola")

buscar_index = cadena1.index("Hola") # nos arroga una expcepcion

primera = cadena1.startswith("g")

primera = cadena1.endswith("o")

remplazar = cadena1.replace (" ", "-") 

contarrepe =  cadena1.count("o")

contarcarac =  len(cadena1)

numerico = cadena1.isalpha() # verifica si es alfanumerico (todo el string tiene que estar pegado)

vernumeric = cadena1.isnumeric() # verifica si el string contiene valores numericos 

convertirLista = cadena1.split(" ")

print(convertirLista)