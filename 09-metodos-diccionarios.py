# agregue un comentario y le archivo de metodos de los diccionarios 

diccionario = {
    "uno": "Hola",
    "dos":"Mundo",
    "subs": "1000000"
}
# nos devulve un objeto dict_item
print(diccionario.keys())

# obteniendo con el metdod de get() (si no encuentra nada el programa continura)
print(diccionario.get("uno"))

#print(diccionario.clear())

print(diccionario.pop("subs", "dos"))

diccinario_iterable = diccionario.items()

print(diccionario_iterable)


