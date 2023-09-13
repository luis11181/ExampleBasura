import pandas as pd  # importa pandas
import numpy as np
import matplotlib as plt

# ? en el notebook de jupiter se piede poner un "!", y asi instalar desde el libro y no terminal todo !pip install -r requirements.txt
# pip install ipykernel   # era para usar jupiter

# *importa un archivo de datos
excel_file_path = r"C:\data\code\aprendiendo\python\bases\cars.csv"  #! toca dejar la r para que sea raw string y lea la url

# !si los datos no son claros puede haber problemas y toca pasar argumentos adicionales
# df = pd.read_csv(excel_file_path) #*lee el archivo con los datos
# df = pd.read_csv(excel_file_path, error_bad_lines=False)  #*salta y elimina los datos que el considere errores
# df = pd.read_csv(excel_file_path,sep='delimiter', header=None) #*asume que no hay headers, y le asigna solo un numero a cada col
# df = pd.read_csv(excel_file_path,skiprows=[2],error_bad_lines=False) #*evita algunas rows filas que le diga debe ir en [x,x], sino evita todo hasta ese numero
# df = pd.read_csv(excel_file_path,sep=';')#* se puede definir el separador que usan las cols de los datos, comunes son: sep=';'sep='\t',sep='/t'
df = pd.read_csv(excel_file_path, skiprows=[1], sep=";")  # los rows inician en 0

#! formas de obtener informacion basica
# df.shape   #da el tamaño de cols, rows
# df.nunique()  # dice la cantidad de datos unicos en col y rows
df.columns
df.head  # encabezados
# df.info()#informacion general
df.describe()  # ?desviacion estandar, count, media, mas datos
# df.describe()['Horsepower'] #*mas info de dato especifico
# print(df.head)
# sample_standard_deviation = df['Horsepower'].std()
# print('desviacion estandar=',sample_standard_deviation)

print("informacion basica=")
print(df.info())
print("descripcion estadistica=")
print(df.describe())

#! define un index, eje x, por defecto es el numero de casilla
# el indice se puede colocar una fecha o otro campo, este sera el eje independiente, estar NO REPETIDO

# *t D = D.set_index('Date') # In this context, Date is the best candidate to be the index

# * reset_index():
# *t reset index quita los indices y deja una tabla normal, con yn indice default

#! eliminar una ffila row , col, crear columnas
# *t eliminar fila
# df = df.drop(df.index[0]) #filas inician en 0
# *t delimina columna
# data = data.drop(labels="deathes", axis=1)  #por nombre
# data = data.drop(columns=data.columns[3]) # por index

# *crear una columna operando datos de otras
# stocks["VolStat"] = (stocks["High"] - stocks["Low"]) / stocks["Open"]


#! groupby , genera grupos y datos con estos y deja sacarle los datos deseados
# grouped_df = df.groupby(['Origin']).max() # los agrupa por caracteristica en el ' ' y escoge el maximo
# * le puede poner .max()  .min()   .mean() para la media  .median()la mediana     .mode() para la moda .size()
# grouped_df['Horsepower'] # da el valor de las cosas agrupadas, dependiendo la caracteristica que escoge, en este caso los maximos horsepower, seleccionando por ogigen los datos  # daria esto Europe     98.00 Japan      97.00 US         98.00

grouped_df = df.groupby(
    ["Origin"]
).max()  # los agrupa por caracteristica en el ' ' y escoge el maximo
grouped_df_da_hp = grouped_df[
    "Horsepower"
]  # da el valor de las cosas agrupadas, dependiendo la caracteristica que escoge, en este caso los maximos horsepower, seleccionando por ogigen los datos  # daria esto Europe     98.00 Japan      97.00 US         98.00
print(grouped_df_da_hp)

# agrupar por 2 factores al tiempo
grouped_plot_df2 = df.groupby(["Origin", "Car"]).mean()


#!! %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#! TRANSFORMAR TIPO
# *para saber el typo de dato que tenemos sirve
# data_types=df.dtypes
# *t CAMBIAR A INT. o date  cambia el tipo de dato para hacer mas facil es trabajo
# *t  transforma datos de string
df["Horsepower"] = df["Horsepower"].astype(int)  # *forma2 con astype
# *t stocks.index = pd.to_datetime(stocks.index)

#!transform string
# * df['commodity_transaction'].str.lower()

#! transformar datos con formulas  apply(),  applymap(), map, transform ,
# *t Summing up, apply works on a row / column basis of a DataFrame, applymap works element-wise on a DataFrame, and map works element-wise on a Series

# *t apply implicitly passes all the columns for each group as a DataFrame to the custom function. while transform passes each column for each group individually as a Series to the custom function.

# *apply       is defined on BOTH
# *t f = lambda x: x.max() - x.min()
# *t frame.apply(f)


# *applymap aplica formula dato a dato, devuelva arreglo mismo tamaño            is defined on DataFrames ONLY
# *t format = lambda x: '%.2f' % x
# *t frame.applymap(format)

# * map                                      is defined on Series ONLY

# * transform
# *t df['Horsepower']=df['Horsepower'].transform(lambda x: int(x)) #*forma1 con transform

transformado = df["Horsepower"].transform(lambda x: x + 100)  # fecorre y hace eso
# transformado2=df['Horsepower'].transform([np.sqrt, np.exp])  #hacerle multiples funciones y da multiples columnas

# *


# *crea otro con unas cols especificas
# si solo se da un argumento en [], se asume que son las columnas
seleccion = df[
    ["Origin", "Horsepower"]
]  # escoge unas rows y cols y crea otro arreglo  [[2,3,4],['Origin','Horsepower']]

#! ELIMINA DATOS REPETIDOS, replace datos
# *t elimina las filas duplicadas de la tabla, basado en una de las columnas
# df["country_or_area"].drop_duplicates()

# *str.replace()
# *t hace el replace de un caracter string
# df['commodity_transaction'].str.lower().str.replace("–", "-")

#! buscar si culple condicion, hacer filtros, transformar tipo dato
# *con condicionales y query
condicion_cars = df[
    df["Horsepower"] == 90
]  # condicion simple, imprime la lista de los true
# df[df["clean_transaction"] == "electricity - imports"].head()

# *t query, permite filtrar tambien de forma mas facil
# df.query('4000< Horsepower < 5000')[:8] #*query('condicion',false o true, si desea cambiar  el array sobre el que esta)[:x] lo 2do es opcional, da los primeros x que cumplen la condicion

# *t  con str.contains se puede filtrar sobre una col solo los que contengan x datos
# *-  df["clean_transaction"][(df["clean_transaction"].str.contains("import"))&(df["clean_transaction"].str.contains("otro_filtro"))].drop_duplicates()

# * Filtering to keep only a array of values
# * .isin()
# *t keep values es un array de string que buscamos, si hace match guarda esas filas
# *t  df_filtered = df[df["commodity_transaction"].isin(keep_values)]

# *con filter
# *t select columns by name, filtra columnas
filter_cars = df.filter(items=["one", "three"])

# select rows containing 'bbi'
filter_cars = df.filter(like="bbi", axis=0)

# * filtra cualquier row que tenga 90 en cualquier campo, como string o int
filter_cars = df.filter(like="90", axis=0)

# print(filter_cars)

# *filtrar y cambiar
largo_df = len(df["Horsepower"])
array_prueba = [130] * largo_df

# cambia los espacios en un array, toma el primero  where( condicion, valor si verdadero,valor si falso)
df["Horsepower"] = np.where(
    df["Horsepower"] > 100, array_prueba, df["Horsepower"]
)  # *a Where True, yield x, otherwise yield y.


# *filtrar una de las columnas por orden
# *nsmallest() and nlargest()    , da los mas pequeños y mas altos de una lista
# df.nsmallest(5,'Horsepower')  # cuantos deseo, de que columna


print(df)

#! Conoattenar pd.concat()  une dos listar o tablas
# pd.concat() Combine two DataFrame objects with identical columns.

# Combine DataFrame objects with overlapping columns and return everything. Columns outside the intersection will be filled with NaN values.

"""
df3 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']],
                   columns=['letter', 'number', 'animal'])
df3
  letter  number animal
0      c       3    cat
1      d       4    dog
pd.concat([df1, df3], sort=False)
  letter  number animal
0      a       1    NaN
1      b       2    NaN
0      c       3    cat
1      d       4    dog
"""

# Combine DataFrame objects with overlapping columns and return only those that are shared by passing inner to the join keyword argument.

"""
pd.concat([df1, df3], join="inner")
  letter  number
"""

#! shift(1) mover una columna
# D["High"].head(5).shift(1)   mueve una de las columnas en una direccion

#! sort
# *t  values_sort=df.sort_values(['Origin','Horsepower'], ascending=[1,1])
# *t  df_countries.sort_values(by="production", ascending=False)

#!insert
# .insert(8,'new_col','new_col)  #(col donde insertar, 'nombre', array con valores)


#! plot
# *plot basico
# df.plot(*args, **kwargs)
# df.plot(x='Origin', y=["Horsepower", "Weight"])
# df.plot.bar(x='Origin', y=["Horsepower", "Weight"])
# *plot con agrupaciones, toca escoger como agrupa ej .count() .mean()  .size() etc...
grouped_plot_df = df.groupby(["Origin"]).mean()  # agrupa
grouped_plot_df.plot(
    y=["Horsepower", "Weight"]
)  # automaicamente imprime por el factor agrupado

# ? ejemplo de plot con title. legend
# stocks.groupby("Symbol")["VolStat"].plot(legend=True,title="Energy Sector Trends - VolStat", figsize=(15,6) )


# *plot con doble agrupacion
# df.groupby(['Origin','Car']).mean()['Horsepower'].unstack(fill_value=0).plot.bar()  #forma1
# pd.crosstab(df['Origin'],df['Car']).plot.bar() # forma2

# print(grouped_plot_df2)
# plt.show()

#! create a pivot table
# *t se le dice que tabla se trabajara, sobre que columna se tomaran los valores y seran puestos en las casillas de los columns escogidos, y cuales seran las columnas de index que iran a la izquiera, se agrupan entre ellas, y finalmente se dice que columnas o culumnas se desean generar, los nombres unicos en ese arreglo se volveran columnas separadas

"""
df_countries = pd.pivot_table(
    df_filtered,
    values="quantity",
    index=["country_or_area", "year"],
    columns="commodity_transaction",
)

df_countries
"""

#!plot de histograma
# se le da una sola columna de valor, y pone frecuencia vs valor
"""
hvm = stocks['Volume_Millions'].plot.hist()

hvm.set_title("Histogram of Volume_Millions")
hvm.set_xlabel("Millions of shares")

plt.plot()
"""

#! export a worked data to excel

# new_export_data = grouped_df_da_hp
# new_export_data.to_excel(r'D:\luis\temas_de_interes\programacion\aprendiendo\python\bases\output.xlsx')

# print(df)

#!!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#! CURSO DS4ALL BASICO DE PANDAS
# * contar un caracter o string en una lista, dice cuantas veces s repite, en que lineas
# df["commodity_transaction"].drop_duplicates().str.count("-").head(10)

# *resumen del count() value_counts()
# *t da el resumen de caracteres repetidos, dice cuantas veces esta y cuantas veces repite por fila
# df["commodity_transaction"].drop_duplicates().str.count("-").value_counts()


# * sumar multiples columnas
# *t  df_countries["renewable_total"] = df_countries[["hydro", "wind", "solar", "geothermal", "tide"]].sum(axis="columns")


#!! %%%%%%%%%%%%%%%%% OTROS  %%%%%%%%%%%%%%%%%%%%%%%%

#! cambiar el typo de datos, si es string a numerico etc..  objeto a int etc...
# *para saber el typo de dato que tenemos sirve
# data_types=df.dtypes
# print(data_types)
# *si son typo objeto nos dan unmetodo que intuye el typo y cambia de tablas
# df_fixed=df.infer_objects()
# print(df_fixed.dtypes)

# si no funciona y se sabe que todos son integers, pero no suele ser el caso
# df_fixed2=df.astype(int)
# print(df_fixed2.dtypes)

# ?por columnas CON AS TYPE
# df['Horsepower']=df['Horsepower'].astype(str, errors='ignore').astype(int, errors='ignore')
# *stocks.index = pd.to_datetime(stocks.index)

# ?por columnas CON pd.to_numeric
# df['Horsepower']=pd.to_numeric(df['Horsepower']) #*si son srtings y se puede convertir
# df['Horsepower']= pd.to_numeric(df['Horsepower'], errors='coerce') #* si hay datos erroneos y toca eliminarlos para pasar el resto a numeros

# print(df_num.describe())


#! variados

# df.isnull()  ans isna() "dice si hay valores null"
# fillna()   cambia todos los nan por 0

# loc: select by labels
# df.loc[:5,['xxx','xxx']]

# print(df.nunique())
