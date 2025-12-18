# promedio de una clase de alumnos
# notas = 3 + 5 + 7 + 2
# division  = notas / 4

# print(f" el promedio de la clase es de {division}")

# def promedio(nota1, nota2, nota3, nota4):
#     suma = (nota1 + nota2 + nota3 + nota4)
#     division = suma / 4
#     return division

# media = promedio(2, 4, 6, 3 )

# media = promedio(3, 34, 32, 56 )

# redondear = round(media,2)

# print(redondear)

#calificacion simple



def rango(nota):
    if nota > 0 and nota <= 5:
        if nota >= 3:
            return("aprobado")
        elif nota < 3:
            return("reprobado")
    elif nota < 0 or nota > 5:
        return "no es un numero valido"

resultado = rango(6)
print(resultado)

