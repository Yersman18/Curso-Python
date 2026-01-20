# EJERCICIOS DE DICCIONARIOS

persona = {
    'nombre': 'Yersman',
    'edad': 19,
    'pais': 'Colombia'
}

# 2 #print(persona['nombre'], persona['pais'])

#3 
persona['edad'] = 20

#print(persona)

#4 
persona['email'] ="yersman@gmail.com"
#print(persona)


#5
for valor in persona:
    resultado = persona.items()
#print(resultado)

#6 

diccionario_nuevo = dict.fromkeys(['Estatura', 'Peso'])

diccionario_nuevo['Estatura'] = 1.72 

# Solo quise agregar un dato para que lo  tengas en cuenta
#print(diccionario_nuevo)

usuarios = [
    {"nombre": "Ana", "edad": 22},
    {"nombre": "Luis", "edad": 25}
]

