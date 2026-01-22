# 🟢 1️⃣ Registro de usuario (realísimo)
# Un sistema recibe este diccionario desde un formulario:

datos = {
    "nombre": "Ana",
    "email": "ana@gmail.com",
    "telefono": 2342424
}

# 👉 Problema real: el teléfono es opcional.
# Tarea:
# crea una función que reciba los datos
# devuelva el teléfono si existe
# si no existe, devuelva "Sin teléfono

clave = "telefono"

def registro(datos, clave):
    if clave in datos:
        return datos[clave]
    else: 
        print('Sin telefono')

registro(datos, clave)

#------------------------------------------------------
#2️⃣ Login de usuario
usuario = {
     "email": "ana@gmail.com",
     "password": 'sadfa'
}

clave1='email'
clave2='password'

# Tarea:
# crea una función que valide:
# que exista email
# que exista password
# si falta algo, devuelve un mensaje claro
# 💡 Esto pasa TODOS los días en sistemas reales.

# def validacion(usuario, email, password):
#     if email and usuario and password in usuario:
#         return "valido" 
#     else:
#         return("falta campos por llenar, verifique la informacion")

# print(validacion(usuario, clave1, clave2))

# si quitamos un campo me va aperecer el error


# 🟡3️⃣ Perfil incompleto
profile = {
    "nombre": "Luis",
    "edad": 17,
    "email": 'yersmangarzon@gmail.com'
}

# Regla del negocio:
# si no hay email, el perfil es incompleto
# Tarea:
# función que devuelva "Perfil completo" o "Perfil incompleto"


def perfil(usuario, email):
    if email in usuario:
        return 'perfil completo'
    else:
        return 'perfil incompleto'
    
resultado = perfil(profile, "email")

print(resultado)







