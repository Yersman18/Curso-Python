# mini sistema que de registro 

# con ese progrma podremos crear un usuario y que pueda iniciar sesión y mirar la lista de los que han podido iniciar sesion 


nombres = []
contraseñas = []


while True:
    print("====MENU PRINCIPAL==== \n" )
    print("1. Registrar usuario ")
    print("2. Inicir sesion")
    print("3. Ver usuario registrados (Requiere login)")
    print("4. Salir ")
    print("5. Prueba de imprimir datos \n ")
    print("====================== \n")
    usuario = int(input("Eliga una opcion: "))
    if usuario == 1:
        print("Escriba los siguientes datos: \n")
        nombre = input("Agregue su nombre: ")
        nombres.append(nombre)
        contraseña = input("Agregue su contraseña: ")
        contraseñas.append(contraseña)
        print("Se registro satisfactoriamente, ya puedes iniciar sesion! \n ")
    if usuario == 2:
        usuario_nombre = input("Ingrese su nombre con el que se registro: ")
        buscar_nombre = nombres.index(usuario_nombre)
        usuario_contraseña = input("Ingrese su contraseña:")
        buscar_contraseña = contraseñas.index(usuario_contraseña)



    # elif usuario == 6:
    #     print(nombres)
    #     print(contraseñas)    
        
    
        