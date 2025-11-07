lista = list(["Hola"]) # nos este metodo podemos crear una lista (este metodo nos sirve mas para crear una lista vacia)

contar = len(lista) # nos cuenta cuantos valores encuentra dentro de la lista

agregando_un_elemento = lista.append("python") # podemos agregar un elemento a la lista

insertando_un_elemento = lista.insert( "2", "java") # podemos agregar un elemento a la lista pero por su ubicacion tambien

agregando_varios_elementos = lista.extend(["js", "html", "23", "02"]) # podemos agregar varios elementos a una lista 

eliminando_por_indice = lista.pop(0) # podemos eliminar un elemento de la lista por su indice 

eliminando_por_valor = lista.remove("js") # podemos eliminar por el contenido del valor

# eliminando_todo = lista.clear() # con este metodo podemos borrar todo lo que hay dentro de la lista 

ordenar = lista.sort() #   # nos organiza la lista de forma  (ascendente reverse= True (Para que orgnize de forma descendente))

revertir = lista.reverse() # asi como esta todos los valores de la lista (asi esten desorganizados) los revierte 




print(lista)



