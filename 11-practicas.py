# Escribí un programa que solicite al usuario que ingrese su nombre. 
# El nombre se debe almacenar en una variable llamada nombre. A continuación 
# se debe mostrar en pantalla el texto “Ahora estás en la matrix, [usuario]”, donde 
# “[usuario]” se reemplazará por el nombre que el usuario haya ingresado.


# nombre = input("Dime tu nombre ") # Aqui le pedimos el nombre al usuario para que lo almacene la variable
# print(f"Ahora esta en la matrix {nombre}") # Aqui imprimimos la respuesta que almacenamos con la variable

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2
# Escribí un programa que solicite al usuario ingresar un número con decimales y almacenalo en una variable. 
# A continuación, el programa debe solicitar al usuario que ingrese un número entero y guardarlo en otra variable. 
# En una tercera variable se deberá guardar el resultado de la suma de los dos números ingresados por el usuario. 
# Por último, se debe mostrar en pantalla el texto “El resultado de la suma es [suma]”, donde “[suma]” se reemplazará 
# por el resultado de la operación.

# primer_numero = float(input("Dame un numero en decimales ")) # Pedimos al usuario que digite el primer numero
# segundo_numero = int(input("Dame un numero entero ")) # Pedimos al usuario que digite el segundo numero
# resultado = (primer_numero + segundo_numero) # Hacemos la operacion correspondiente

# print(f"El resultado de la suma es {resultado}") # imprimos la respuesta con la respuesta de la variable de "resultado"

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3  Escribí un programa que solicite al usuario dos números y los almacene en dos variables. En otra variable, 
#almacená el resultado de la suma de esos dos números y luego mostrá ese resultado en pantalla.
#A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en una nueva variable. 
#Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.

# numero_uno = int(input("Digite su primer numero "))
# numero_dos = int(input("Digite su segundo numero "))

# suma = numero_uno + numero_dos

# resultado_suma = print(f"La suma de los dos numeros que digito es {suma}")

# numero_tres = int(input("aqui ingrese su nuevo numero para multiplicarlo por la suma de los dos primeros numeros: "))

# resultado_final = print("La multiplicacion del nuevo numero ingresado por la suma de los dos primeros numeros es de" , numero_tres * suma)

#------------------------------------------------------------------------------------------------------------------------------------------------------------


# Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por una motocicleta y la cantidad de
# litros de combustible que consumió durante ese recorrido. Mostrar el consumo de combustible por kilómetro.

# kilometro_recorridos = int(input("Dime cuantos kilometros recorriste en tu motocicleta: "))
# litros_combustible = int(input("Dime la cantidad de litros de combustible que consumiste: "))

# resultado = (print("El consumo de combustible por kilometro es de ",kilometro_recorridos/litros_combustible,"litros"))


#------------------------------------------------------------------------------------------------------------------------------------------------------------

#Escribí un programa que solicite al usuario el ingreso de una temperatura en escala Fahrenheit (debe permitir decimales) y le muestre el equivalente en grados Celsius. 
#La fórmula de conversión que se usa para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32)_
 

# Fahrenheit = int(input("ingresa una temperatura en escala Fahrenheit: "))

# convertir = Fahrenheit - 32

# division_fahrenheit = 5 / 9

# multiplicacion_celcius = division_fahrenheit * convertir

# print(f"la conversion de la temperatura en Celcius es de {multiplicacion_celcius:.2f}")

tupla = ("estebabn", "Daniel")

print(type(tupla))