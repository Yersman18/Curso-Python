nombres = ["ESTEBAN", "Paula"]
usuario = input("Escribe un nombre ")
encontrado = False

for nombre in nombres:
    if nombre == usuario:
        print("Este nombre ya esta registrado:")
        encontrado = True
        break
if not encontrado:
    print("No puedes acceder este nombre al sistema")