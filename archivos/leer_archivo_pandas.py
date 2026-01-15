import pandas as pd

df = pd.read_csv("archivos\\datos.csv",) #names=['name','lastname','age'])
df2 = pd.read_csv("archivos\\datos.csv",)


# obteniendo los nombres del archivo
#print(df['nombres'])

#cadena = "012345678"

# este nos funciona para que nos aparezca en un rango y tambien nos funciona de la a hasta la z 
#print(cadena[:]) # esto es lo mas importante para nosotros (:)


# nos organiza el dataframe por la edad
df_ordenado = df.sort_values("edad")

#ordenandolo de forma descendente (nos organiza la edad de forma que la edad mayor va de primeras)
df_ordenado = df.sort_values("edad", ascending=False)

#concatenando los dos dataframes y nos arroga todos los daos en un solo
df_concatenando = pd.concat([df, df2])

# accediendo a las primeras 3 filas con head()
primer_fila = df.head(3)


# accediendo a las ultimas 3 filas con tail()
ultima_fila = df.tail(3)

# accediendo a la cantidad de filas  y columnas con shape
#filas_columanas_totales = df.shape


# desempaquetamos el archivo para poder acceder a cada fila y columna con shape
filas_totales, columnas_totales = df.shape

#accediendo a un elemento especifico del df con loc 
# accedemeos a un elemento especifico
elemento_especifico_loc = df.loc[2,"nombres"]

# accedemos de la misma manera pero con el indice 
elemento_especifico_iloc = df.iloc[2,0]

#accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con loc
nombres = df.iloc[2,:]

#accediendo a filas con edad mayor que 30
mayor_que_30 = df.loc[df["edad"]>30,:]

print(mayor_que_30)





