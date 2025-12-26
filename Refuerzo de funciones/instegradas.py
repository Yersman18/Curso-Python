# promedio de una clase de alumnos
# notas = 3 + 5 + 7 + 2
# division  = notas / 4

# print(f" el promedio de la clase es de {division}")

# def promedio(nota1, nota2, nota3, nota4):
#     suma = (nota1 + nota2 + nota3 + nota4)
#     division = suma / 4
#     return division

# media = promedio(2, 4, 6, 3 )

# media = promedio(3, 34, 32, 56 )

# redondear = round(media,2)

# print(redondear)

#calificacion simple

# def rango(nota):
#     if nota > 0 and nota <= 5:
#         if nota >= 3:
#             return("aprobado")
#         elif nota < 3:
#             return("reprobado")
#     elif nota < 0 or nota > 5:
#         return "no es un numero valido"

# resultado = rango(6)
# print(resultado)


#👌 ejercicios sencillos 1

# crea una funcion que reciba un numero y retorne el doble


# def doble(numero):
#     dobles = numero * 2
#     return dobles

# numero = int(input("Escribe un numero: "))

# resultado = doble(numero)

# print(resultado)


# Crea una funcion que reciba un nombre y retorne un saludo


# def saludo (nombre):
#     return(f"Hola {nombre} como estas espero que tengas un excelente dia")

# nombre = input("Dime tu nombre para poder saludarte: ")

# resultado = saludo(nombre)

# print(resultado)



# crea una funcion que reciba una edad y retorne mayor de edad o menor de edad:

# def edad(años):
#     if años  >= 18:
#         return "eres mayor de edad"
#     else:
#         return "eres menor de edad"



# años = int(input("escribe tu edad: "))
# resultado = edad(años)
# print(resultado)


# crea una funcion que reciba dos numeros y retorne el menor

# def numero_menor(num1, num2):
#     if num1 > num2:
#         return "el primer numero es mayor que el segundo"
#     elif num1 == num2:
#         return "los dos numeros son iguales"
#     else:
#         return "El segundo numero es mayor que el primero"

# num1 = int(input("Escribe un numero: "))
# num2 = int(input("Escribe otro numero: "))

# resultado = numero_menor(num1, num2)

# print(resultado)


# EJERCICIO 5 

# crea una funcion que reciba una nota de (0-5) y retorne:
# "Excelente" (>=4)
# "Aprobado" (>=3)
# "Reprobado" (<3)

# def notas(nota):
#     if nota >= 4:
#         return "Excelente"
#     elif nota >= 3:
#         return "Aprobado"
#     else:
#         return "Reprobado"
    
# num = int(input("Escribe una nota: "))
# resultado = notas(num)

# print(resultado)

# EJERCICIOS CON LISTAS

# def suma_total (numeros):


numeros = []
numero = 0


for numero in range(3):
    numero = int(input("ingresa un numero: "))
    ingresar = numeros.append(numero)
    suma = sum(numeros)
print(suma)


