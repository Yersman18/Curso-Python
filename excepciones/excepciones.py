
# creando una funcion que suma numeros
def sumar_dos():
    while True:
        #pidiendo numeros
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        # intentando convertirlos en enteros y sumarlos
        try:
            resultado = int(a) + int(b)
        # si lanzon una excepcion pedirle que reingrese los datos
        except ValueError as e: #  (except ValueError as e:)
            print("Te pedi un numero, no un caracter ")
            print(f"ERROR {e}")
        # si todo salio bien terminamos el programa
        else:
            break
        # se utiliza rara vez esta funcion
        finally: 
            print("siempre se va a ejecutar ")
    # retornamos el resultado de la operacion   
    return resultado

print(sumar_dos())
