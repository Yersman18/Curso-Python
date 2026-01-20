# creando un diccionario
persona = {
    'nombre': 'Yersman ' 'Esteban',
    'Edad': 19,
    'Lugar de residencia': 'Madrid Cundinamarca'
}

#print(persona['nombre']) nos arroga el valor de la clave

#print(persona.keys()) # nos arrgoa el nombre de las claves

#print(persona.get('nombre')) # ponemos la clave y nos arroga el valor que contiene esa clave

eliminando = persona.pop('Edad')

print(persona.items())

# -------------------------------------DICCIONARIOS 2.0
# creando diccionarios con dict()

diccionario = dict(nombre="Esteban", apellido = "Garzon")

diccionario_nuevo = dict.fromkeys({'Estatura', 'Peso'}) # Creamos un diccionario vacio

agregando_datos = diccionario_nuevo['Estatura'] = 1.70 # Agregamos un valor al diccinario creado

print(diccionario_nuevo)


