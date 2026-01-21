# #print(diccionario)

# def usuario(nombre_usuario, edad_usuario, email_usuario):
#     persona = dict.fromkeys({'nombre', 'edad','email'})
#     persona['nombre'] = nombre_usuario
#     persona['edad'] = edad_usuario
#     persona['email'] = email_usuario
#     return persona

# nombre_usuario = input('Escribe tu nombre: ')
# edad_usuario = int(input('Escribe tu edad: '))
# email_usuario = input('Escribe tu email: ')

# resultado = usuario(nombre_usuario, edad_usuario, email_usuario)


# print(resultado)#accedemos al valor de la clave


# #def persona(nombre, edad):


#EJERCICIO 1 
# Objetivo: perderle el miedo a crear diccionarios en funciones.
# Enunciado
# Crea una función llamada crear_persona que reciba:
# nombre
# edad
# ciudad
# La función debe retornar un diccionario con esos datos.
# Ejemplo de salida:
# {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Bogotá'}


# def crear_persona(nombre, edad, ciudad):
#     persona = {
#         'nombre': nombre,
#         'edad': edad,
#         'ciudad': ciudad
#     }
#     return persona

# nombre = input("Escribe tu nombre: ")
# edad = int(input("Escribe tu edad: "))
# ciudad = input("Escribe tu ciudad: ")

# resultado = crear_persona(nombre, edad, ciudad)


#EJERCICIO 2
# Objetivo: aprender a usar el diccionario que devuelve la función.
# Enunciado
# Usando el diccionario del ejercicio anterior:
# Imprime solo el nombre
# Imprime solo la edad
# 🔹 Pista:
# Usa resultado['nombre']
# No vuelvas a pedir datos

# print(resultado['nombre'])
# print(resultado['edad'])

#EJERCICIO 3

# for clave, valor in resultado.items():
#     print( clave, valor )


#EJERCICIO 4
# Objetivo: dejar de pensar solo en “crear” y empezar a usar diccionarios.
# Enunciado
# Crea una función llamada mostrar_persona que:
# Reciba un diccionario persona
# Imprima todos sus datos (clave y valor)


persona = {
    'nombre': 'esteban',
    'edad': 19
}

def mostrar_persona(persona):
    for clave, valor in persona.items():
        print (clave, valor)
    
mostrar_persona(persona)


#EJERCICIO 5

