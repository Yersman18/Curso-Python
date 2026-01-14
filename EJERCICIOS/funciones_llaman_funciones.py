#EJERCICIO 
# Crea una funcion que reciba un numero y retorne true si es par y false si es impar
# Otra funcion que reciba una lista de numeros y use la funcion anterior para retornar solo los numeros pares

# numeros = []

# def par_impar(numeros):
#     numeros_impares_pares = []
#     for num in numeros:
#         if num % 2 == 0:
#             numeros_impares_pares.append(True)
#         elif num % 2 != 0:
#             numeros_impares_pares.append(False)
#     return numeros_impares_pares

# def pares(numeros_impares_pares):
#     numeros_pares = []
#     for num_par in numeros_impares_pares:
#         if num_par % 2 == 0:
#             numeros_pares.append(num_par)
#     return f"Y LA CLASIFICACION DE LOS NUMEROS PARES SON: {numeros_pares}"


# for numero in range(3):
#     usuario = int(input("Ingresa un numero: "))
#     numeros.append(usuario)

# resultado1 = par_impar(numeros)

# print(resultado1)




## EJEMPLO DE FUNCIONES COMBINADAS
# Función 1: recibe UN número y dice si es par
def es_par(numero):
    return numero % 2 == 0


# Función 2: recibe una lista y usa la función anterior
def obtener_pares(lista):
    numeros_pares = []
    for num in lista:
        if es_par(num):          # aquí se llama la otra función
            numeros_pares.append(num)
    return numeros_pares


# ----- Programa principal -----
numeros = []

for _ in range(3):
    usuario = int(input("Ingresa un número: "))
    numeros.append(usuario)

resultado = obtener_pares(numeros)
print(resultado)




