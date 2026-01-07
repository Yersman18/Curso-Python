# Crea una funcion que reciba un numero y retorne su cuadrado

# def cuadrado(numero):
#     return numero * numero


# usuario = int(input("Ingresa un numero: "))
# #Utilzando la funcion que quiera
# resultado = cuadrado(usuario)
# print(f"El cuadrado del {usuario} es {resultado}")

# ya los primeros ejercicios ya los hice voy hacer los del nivel 2

#NIVEL 2

# crea una funcion que reciba uan lista de numeros y retorne la suma

# lista_num = []
# usuario = 0
# contar = 0

# while 3 > contar:
#     usuario = int(input("Ingresa un numero: "))
#     lista_num.append(usuario)
#     contar = len(lista_num)

# #print(lista_num)
# def sumar_lista(lista):
#     return sum(lista)

# resultado = sumar_lista(lista_num)

# print(resultado)

# 2. Crea una función que reciba una lista y retorne el promedio.

# limite = int(input("Escribe cuantas notas vas a ingresar: "))
# notas = []
# contar = 0

# while limite > contar:
#     nota = float(input("ingresa una nota: "))
#     notas.append(nota)
#     contar = len(notas)

# def promedio(calificaciones, num_notas):
#     suma_total =  sum(calificaciones)
#     return suma_total / num_notas

# resultado = promedio(notas, contar)

# print(round(resultado, 2))

# Sumar todos los números de una lista

# numeros = []

# def suma_total(numeros):
#     return sum(numeros)

# for numero in range(3):
#     num = int(input("Ingresa un numero: "))
#     numeros.append(num)

# resultado = suma_total(numeros)
# print(resultado)

# Retornar solo los números pares

# numeros_pares = []


# def pares(numeros_pares):
#     numeros = []

#     for num in numeros_pares:
#         residuo = num % 2
#         if residuo == 0:
#             numeros.append(num)
#     return numeros 


# for numero in range(4):
#     usuario = int(input("ingresa un numero: "))
#     numeros_pares.append(usuario)    


# resultado = pares(numeros_pares)

# print(resultado)


#-------------------------2 funcion que retorne los numeros mayores que 10

# numeros = []

# def mayor(numeros):
#     numeros_mayor = []
#     for num in numeros:
#         if num > 10:
#             numeros_mayor.append(num)
#     return numeros_mayor
    
# for num in range(5):
#     num = int(input("Escribe un numero: "))
#     numeros.append(num)

# resultado = mayor(numeros)

# print(resultado)

#-----------------------------------------------------
# retorna solo los numeros negativos

# numeros = []

# def negativos(numeros):
#     numeros_negativos = []
#     for numero in numeros:
#         if numero <= 0:
#             numeros_negativos.append(numero)
#     return numeros_negativos

# for num in range(5):
#     usuario = int(input("Ingrese un numero: "))
#     numeros.append(usuario)

# resultado = negativos(numeros)

# print(resultado)

#-------------------------------------------------

# Retorne una palabra que mas de 5 caracteres


# palabras = []

# def caracteres(palabras):
#     nuevas_palabras = []
#     for car in palabras:
#         contar = len(car)
#         if contar > 5:
#             nuevas_palabras.append(car)
#     return nuevas_palabras

# for palabra in range(4):
#     usuario = input("Ingresa una palabra: ")
#     palabras.append(usuario)


# resultado = caracteres(palabras)

# print(resultado)

# EJERCICIO 3
# RETORNE LOS NUMEROS MPARES MAYORES QUE 10 

# numeros = []

# def numeros_cla(numeros):
#     numeros_nuevos = []
#     for num in numeros:
#         if num % 2 == 0 and num > 10:
#             numeros_nuevos.append(num)
#     return numeros_nuevos

# for numero in range(3):
#     usuario = int(input("Escriba un numero: "))
#     numeros.append(usuario)

# resultado = numeros_cla(numeros)
# print(resultado)

#EJERCICIO
# retorna nombres que empiecen por una letra

# nombres = []

# def inicial(nombres):
#     in_nombres = []
#     for nom in nombres:
#         initial = nom.find("A")
#         if initial == 0:
#             in_nombres.append(nom)
#     return in_nombres

# for nombre in range(3):
#     usuario = input("ingresa un nombre: ")
#     nombres.append(usuario)

# resultado = inicial(nombres)

# print(resultado)



