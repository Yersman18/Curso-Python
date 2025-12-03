

# recorriendo la lista de animales
animales = ["gato" "perro", "cocodrilo", "leon"]

for animal in animales:
    print(f"ahora la variable animal nos imprimi {animal}")


# recorriendo la lista de numeros
numeros = [2, 2, 5, 7]

for numero in numeros:
    operacion = numero * 2 
    print(operacion)

#iterando dos listas

for numeros, animales in zip(numeros, animales):
    print(f"Esta es la lista 1: {animales}")
    print(F"Esta es la lista 2: {numeros}")

#FORMA NO CORRECTA PARA NO RECORRER UNA LISTA
#for num in range(len(numeros)): 
#   print(numeros[num])


for num in  enumerate(numeros):
    print(num[1])
