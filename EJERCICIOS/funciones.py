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

limite = int(input("Escribe cuantas notas vas a ingresar: "))
notas = []
contar = 0

while limite > contar:
    nota = float(input("ingresa una nota: "))
    notas.append(nota)
    contar = len(notas)

def promedio(calificaciones, num_notas):
    suma_total =  sum(calificaciones)
    return suma_total / num_notas

resultado = promedio(notas, contar)

print(round(resultado, 2))

# 3. Crea una función que reciba una lista y retorne el número mayor.






# 4. Crea una función que reciba una lista y cuente cuántos números son pares.

# 5. Crea una función que reciba una lista y retorne una nueva lista solo con los números mayores a 10.


