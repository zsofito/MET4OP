import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

#Importamos el archivo
database_original = pd.read_csv('datos_agrup.csv')

#Me quedo con los datos de "CONSENSO FEDERAL"
database = database_original[database_original.NOMBRE_AGRUPACION == "CONSENSO FEDERAL"]
database.head()
#Observamos los primeros 3
database.head(20)
#Vemos cómo está compuesta la base de datos
print("La base de datos tiene " + str(database.shape[0]) + " filas y " + str(database.shape[1])+ " columnas. Las columnas son:")
for i in range(len(database.columns)):
    print(database.columns[i])
#Vemos los tipos de datos de las columnas
database.info()
#Contamos cuántos nulls hay
database.isnull().sum()

#Vemos cuántas mesas hay
database.CODIGO_MESA.value_counts().sum()

#Vemos cuántos votos sacó Consenso Federal
database.VOTOS_AGRUPACION.sum()
#Agrupamos los votos y las comunas y sacamos un promedio de voto por comuna 
database_agrupado_comuna = database.groupby("NOMBRE_REGION").VOTOS_AGRUPACION.sum()
print("La cantidad de votos promedio por comuna es de: " + str(np.around(database_agrupado_comuna.values.mean())))

