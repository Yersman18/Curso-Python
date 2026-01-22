#creando un diccionario vacio 
usuario = dict.fromkeys(['Nombre:', 'Apellidos:', 'Ciudad Natal:', 'Telefono:' ])

#print(usuario['Nombre*:']) # None

#agregamos el valor a la clave 
#usuario['Nombre'] = input('Nombre: ')

claves = dict.keys(usuario)
#print(claves)

for i in claves:
    usuario[i] = input(i)

print(usuario)