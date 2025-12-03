# Pide un número y repítelo 5 veces en pantalla.

# numero_usuario = input("Dame un numero: ")

# for i in numero_usuario:
#     print (numero_usuario * 5)

#-------------------------------------------------------------------------------
# Contar del 1 al número que ingresa el usuario

# ingresar_usuario = int(input("Ingresa un numero: "))

# for i in range(0, ingresar_usuario):
#     print( i + 1)

#-------------------------------------------------------------------------

# Pedir una palabra y mostrarla letra por letra

# palabra_usuario = input("Dame una una palabra")

# for i in palabra_usuario:
#     print(i)

#------------------------------------------------------------------

# Imprime los números del 1 al 20.


# for i in range(1,20):
#     print(i + 1)

# Imprime solo los números pares entre 0 y 30.   

# for i in range(0,30,2):
#     print(i)

# Muestra los números del 20 al 0 en orden descendente.
# for i in range(20, 0, -1):
#     print(i)


# Recorre una lista de animales y muestra cada uno

# lista = ["Gato", "Perro", "Oso"]

# for i in lista:
#     print(i, end=" ")


#Muestra cuántas letras tiene cada palabra de una lista de nombres

lista = ["Esteban", "Sebastian", "Diego"]

# for i in lista:
#     contar = len(i)
#     print(contar) 

# Calcula cuántos números negativos hay en una lista.
# numeros = [-3, 2, 4, -1, -34]

# for i in numeros:
#     if i < 0:
#         print(i)


#--------------------------------------------------------------------

# print("diga si, si desea continuar con el programa")

# pregunta = input("Desesea continuar con el programa: ")

# while pregunta == "si":
#     pregunta = input("Desesea continuar con el programa: ")
#     if pregunta == "no":
#         print("fin del programa")

#--------------------------------------------------------------

# Escriba un programa que solicite una contraseña 
# (el texto de la contraseña no es importante) y la vuelva a
#  solicitar hasta que las dos contraseñas coincidan.

# contraseña =  input("dame tu contraseña: ")
# repetir_contraseña= input("dame de nuevo tu contraseña: ")

# while contraseña != repetir_contraseña:
#     repetir_contraseña = input("la contraseña no es la misma, digite de nuevo la contraseña: ")
# if contraseña == repetir_contraseña:
#     print("la contraseña es igual MUY BIEN!")


#Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la 
#"vuelva a solicitar hasta que las dos contraseñas coincidan, con un límite de tres peticiones

# contraseña = input("Escribe tu contraseña: ")
# print ("Tiene tres intentos para escribir su contraseña")
# repetir_contraseña = input("repita la contraseña:")

# intento_max = 2
# intentos = 0

# while contraseña != repetir_contraseña and intentos < intento_max:
#     intentos += 1
#     repetir_contraseña = input("repita la contraseña se equivoco :")
# if contraseña == repetir_contraseña:
#     print("Contraseña correcta")
# else:
#     print("se agotaron los intentos ")


