# mini sistema que de registro 

# con ese progrma podremos crear un usuario y que pueda iniciar sesión y mirar la lista de los que han podido iniciar sesion 


nombres = []
contraseñas = []
encontrado = False

#0 para poder imprimir la lista de nombres 
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
        usuario = input("Agregue su nombre:")
        for nombre in nombres:
            if usuario != nombre:
                nombres.append(usuario)
            else:
                print("El nombre no es correcto")
        

            


    if usuario == 0:
        print(nombres)
    
        

        

        
    #     print("Se registro satisfactoriamente, ya puedes iniciar sesion! \n ")
    # elif usuario == 2:
    #     usuario_nombre = input("Ingrese su nombre con el que se registro: ")
    #     buscar_nombre = nombres.index(usuario_nombre)
    #     usuario_contraseña = input("Ingrese su contraseña:")
    #     buscar_contraseña = contraseñas.index(usuario_contraseña)
    #     print("pudiste iniciar sesión!")
    




    # elif usuario == 6:
    #     print(nombres)
    #     print(contraseñas)    
        
    
        