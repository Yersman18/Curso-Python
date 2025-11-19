#Para tributar un determinado impuesto se debe ser mayor de 16 años 
#y tener unos ingresos iguales o superiores a 1000 € mensuales. 
#Escribir un programa que pregunte al usuario su edad y sus ingresos
#mensuales y muestre por pantalla si el usuario tiene que tributar o no.


# edad = int(input("Introduce tu edad: "))
# ingresos_mensuales = int(input("Dame tus ingress mensuales:"))


# if edad >= 16 and ingresos_mensuales >= 1000:
#     print("Si tienes que tributar")
# else:
#     print("No tienes que  tributar") 


#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo 
#al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre 
#anterior a la M y los hombres con un nombre posterior a la N y el grupo B 
#por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, 
#y muestre por pantalla el grupo que le corresponde.

#nombre = input("Dame tu nombre: ")
#sexo = input("Dime cual es tu sexo (F o M): ")

#if (nombre[0].lower() < "m" and sexo.lower() == "f") or (nombre[0].lower() > "n" and sexo.lower() == "m":)
#    print("perteneces al grupo A")
#else 
    #print("pertences al grupo B")


# En una determinada empresa, sus empleados son evaluados al final de cada año. 
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
# traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden 
# ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. 
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. 
# La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación 
# del nivel.

# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	0.4
# Meritorio	0.6 o más


# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, 
# así como la cantidad de dinero que recibirá el usuario.

# puntuacion_usuario = float(input("Dame tu puntuacion: "))
# dinero = puntuacion_usuario * 2400

# if puntuacion_usuario == 0.0:
#     print(f"Inaceptable y recibiras {dinero}")
# elif puntuacion_usuario == 0.4:
#     print(f"aceptable y recibiras {dinero}")
# elif puntuacion_usuario >= 0.6:
#     print(f"meritorio y recibiras {dinero}")


# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y 
# quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 
# 5€ y si es mayor de 18 años, 10€.


# cliente = int(input("ingresa tu edad para saber el precio de tu entrada: "))

# if cliente < 4:
#     print("puedes entrar gratis")
# elif cliente >= 4 and cliente <= 18:
#     print("Debes pagar una entreda de 5 euros")
# elif cliente > 18:
    # print("Debes pagar una entrada de 10 euros")


# Ejercicio 10
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
# Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para 
# que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que 
# están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es 
# vegetariana o no y todos los ingredientes que lleva.

pizza = input("quieres una pizza vetariana? n/s ")

ingrediente_uno = "Pimiento"
ingrediente_dos = "Tofu"

ingrediente_uno_no ="Peperoni"
ingrediente_dos_no = "jamon"
ingrediente_tres_no = "salmon"


if pizza == "s":
    ingrediente = int(input("Estos son los ingredientes, elige uno: \n1: Pimiento \n2: Tofu \n"))
    if ingrediente == 1:
        print(f"Tu pizza contiene tomate queso y {ingrediente_uno} y es vegetariana")
    elif ingrediente == 2:
            print(f"Tu pizza contiene tomate queso y {ingrediente_dos}")
elif pizza == "n":
    ingrediente = int(input("Estos son los ingredientes, elige uno: \n 1: Peperoni \n 2:jamon \n 3: Salmon"))
    if ingrediente == 1: 
        print(f"Tu pizza contiene tomate queso y {ingrediente_uno_no} y no es vegetariana")
    elif ingrediente == 2:
            print(f"Tu pizza contiene tomate queso y {ingrediente_dos_no} y no es vegetariana")
    elif ingrediente == 3:
                print(f"Tu pizza contiene tomate queso y {ingrediente_tres_no} y no es vegetariana")

