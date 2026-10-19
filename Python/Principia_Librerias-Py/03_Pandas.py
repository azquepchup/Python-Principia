import pandas as pd
sep = "=" * 120


print(pd.__version__)


#* Serie: Es como una matriz etiquetada unidimencional (es como una columna en una hoja de calculo)

data = [100, 204, 21]

series = pd.Series(data) #Los datos se organizan en una columna y se enumera

print(series)  #Imprime la serie y dice que tipo de metadato es en este caso dice que es un int de 64 bits, su tuviera float pondria float64, funciona igual para cualquier tipo, pueden ser obj, boolianos, etc
print(sep)

data_2 = [100, "A", False, 1/2]

series_2 = pd.Series(data_2, index= ["a", "b", "c", "d"]) #Etiquetas

print(series_2)

print(series_2.loc["a"]) #Devuelve el valor de la etiqueta
print(series_2.iloc[1]) #Devuelve el valor de la posición, en este caso el de la posición 1

print(sep)

Numeros = [10, 20, 41, 194, 129412, 1239, 12, 204, 121, 249, 48, 915]

N_series = pd.Series(Numeros, index= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m"])

print(N_series)
print(N_series[N_series >= 200])

print(sep)
#* Tambien se puede para dias
calorias = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}

series = pd.Series(calorias) #Al hacerlo diccionario automaticamente la enumeración para este caso seria Day 1, Day 2 etc

series.loc["Day 2"] += 500 #Sume 500 al valor en Day 2
print(series)
print(series.loc["Day 2"])
print(series[series < 2000])

print(sep)
# * DataFrames: Es una estructura de datos con filas y columnas es bisimensional similar a una hoja de calculo de excel

Datos = {"Name" : ["Juan", "Carlos", "Daniel", "Jose", "Ronaldo"], #Aqui pongo datos de nombre esta sera la etiqueta de la columna y sus datos respectivamente 
            "Edad" : [30, 10, 20, 38, 58] #Igual que el anterior etiqueta de la columna y datos de cada 
}

df = pd.DataFrame(Datos, index= ["Empleado 1", "Empleado 2", "Empleado 3", "Empleado 4", "Empleado 5"]) #index es para poner etiquetas a las filas
print(df)

print(df.loc["Empleado 1"]) # veo la info pip install pylsp-rope --break-system-packagesde uno solo, escribiendo la etiqueta de su fila
print(df.iloc[2]) #* Veo la info de uno solo, escribiendo la posición

#* Añardir una nueva columna 
df["Puesto"] = ["Cocinero", "Capacitación", "Cajero", "Mesero", ""]
