import pandas as pd # importa pandas
import numpy as np
import matplotlib.pyplot as plt
#pip install ipykernel

#*importa un archivo de datos
excel_file_path = r'C:\Users\luis1\Downloads\cars.csv' #! toca dejar la r para que sea raw string y lea la url

# !si los datos no son claros puede haber problemas y toca pasar argumentos adicionales
#df = pd.read_csv(excel_file_path) #*lee el archivo con los datos
#df = pd.read_csv(excel_file_path, error_bad_lines=False)  #*salta y elimina los datos que el considere errores
#df = pd.read_csv(excel_file_path,sep='delimiter', header=None) #*asume que no hay headers, y le asigna solo un numero a cada col
#df = pd.read_csv(excel_file_path,skiprows=[2],error_bad_lines=False) #*evita algunas rows filas que le diga debe ir en [x,x], sino evita todo hasta ese numero
#df = pd.read_csv(excel_file_path,sep=';')#* se puede definir el separador que usan las cols de los datos, comunes son: sep=';'sep='\t',sep='/t'
df = pd.read_csv(excel_file_path) # los rows inician en 0 ,skiprows=[1],sep=';'


#! formas de obtener informacion basica
df.columns
df.head #encabezados
#df.info()#informacion general
df.describe()# ?desviacion estandar, count, media, mas datos
#df.describe()['Horsepower'] #*mas info de dato especifico
#print(df.head)
#sample_standard_deviation = df['Horsepower'].std()
#print('desviacion estandar=',sample_standard_deviation)

print('informacion basica=')
print(df.info())
print('descripcion estadistica=')
print(df.describe())






#! eliminar una ffila row , col
#eliminar fila
#df = df.drop(df.index[0]) #filas inician en 0
#delimina columna
#data = data.drop(labels="deathes", axis=1)  #por nombre
#data = data.drop(columns=data.columns[3]) # por index

#! groupby , genera grupos y datos con estos y deja sacarle los datos deseados
#grouped_df = df.groupby(['Origin']).max() # los agrupa por caracteristica en el ' ' y escoge el maximo
# le puede poner .max()  .min()   .mean() para la media  .median()la mediana     .mode() para la moda .size()
#grouped_df['Horsepower'] # da el valor de las cosas agrupadas, dependiendo la caracteristica que escoge, en este caso los maximos horsepower, seleccionando por ogigen los datos  # daria esto Europe     98.00 Japan      97.00 US         98.00

#?grouped_df = df.groupby(['Origin']).max() # los agrupa por caracteristica en el ' ' y escoge el maximo
#?grouped_df_da_hp = grouped_df['Horsepower']
#  da el valor de las cosas agrupadas, dependiendo la caracteristica que escoge, en este caso los maximos horsepower, seleccionando por ogigen los datos  # daria esto Europe     98.00 Japan      97.00 US         98.00
#?print(grouped_df_da_hp)

#*agrupar por 2 factores al tiempo
#grouped_plot_df2=df.groupby(['Origin','Car']).mean()


#! TRANSFORMAR
#*CAMBIAR A INT. cambia el tipo de dato para hacer mas facil es trabajo
#df['Horsepower']=df['Horsepower'].transform(lambda x: int(x)) #*forma1 con transform
#?df['Horsepower']=df['Horsepower'].astype(int) #*forma2 con astype

#*transforma datos operaciones matematicas
#?transformado=df['Horsepower'].transform(lambda x: x + 100)# fecorre y hace eso
#transformado2=df['Horsepower'].transform([np.sqrt, np.exp])  #hacerle multiples funciones y da multiples columnas

#*crea otro con unas cols especificas
#seleccion= df[[0,1,2,3,4,5],['Origin','Horsepower','Car']]# escoge unas rows y cols y crea otro arreglo

#! buscar si culple condicion, hacer filtros, transformar tipo dato
#*con condicionales
#?condicion_cars =df[df['Horsepower']==90] #condicion simple, imprime la lista de los true

#*con filter
# select columns by name, filtra columnas
#?filter_cars=df.filter(items=['one', 'three'])

# select rows containing 'bbi'
#?filter_cars=df.filter(like='bbi', axis=0)

# filtra cualquier row que tenga 90 en cualquier campo, como string o int
#filter_cars=df.filter(like='90', axis=0)

#*filtrar y cambiar
#largo_df= len(df['Horsepower'])
#array_prueba=[130]*largo_df

#cambia los espacios en un array, toma el primero  where( condicion, valor si verdadero,valor si falso)
#df['Horsepower'] = np.where(df['Horsepower'] > 100, array_prueba , df['Horsepower']  )  #*Where True, yield x, otherwise yield y.

#print(df)

#! sort
#values_sort=df.sort_values(['Origin','Horsepower'], ascending=[1,1])


#! plot
#*plot basico
#df.plot(*args, **kwargs)
#df.plot(x='Origin', y=["Horsepower", "Weight"])
#df.plot.bar(x='Origin', y=["Horsepower", "Weight"])
#*plot con agrupaciones, toca escoger como agrupa ej .count() .mean()  .size() etc...
#?grouped_plot_df = df.groupby(['Origin']).mean() #agrupa
#?grouped_plot_df.plot( y=["Horsepower", "Weight"])#automaicamente imprime por el factor agrupado


#*plot con doble agrupacion
#df.groupby(['Origin','Car']).mean()['Horsepower'].unstack(fill_value=0).plot.bar()  #forma1
#pd.crosstab(df['Origin'],df['Car']).plot.bar() # forma2

#print(grouped_plot_df2)
#plt.show()



#! export a worked data to excel

#new_export_data = grouped_df_da_hp
#new_export_data.to_excel(r'D:\luis\temas_de_interes\programacion\aprendiendo\python\bases\output.xlsx')

#print(df)




#! %%%%%%%%%%%%%%%%% OTROS  %%%%%%%%%%%%%%%%%%%%%%%%

#! cambiar el typo de datos, si es string a numerico etc..  objeto a int etc...
# *para saber el typo de dato que tenemos sirve
#data_types=df.dtypes
#print(data_types)
#*si son typo objeto nos dan unmetodo que intuye el typo y cambia de tablas
#df_fixed=df.infer_objects()
#print(df_fixed.dtypes)

# si no funciona y se sabe que todos son integers, pero no suele ser el caso
#df_fixed2=df.astype(int)
#print(df_fixed2.dtypes)

#?por columnas CON AS TYPE
#df['Horsepower']=df['Horsepower'].astype(str, errors='ignore').astype(int, errors='ignore')

#?por columnas CON pd.to_numeric
#df['Horsepower']=pd.to_numeric(df['Horsepower']) #*si son srtings y se puede convertir
#df['Horsepower']= pd.to_numeric(df['Horsepower'], errors='coerce') #* si hay datos erroneos y toca eliminarlos para pasar el resto a numeros

#print(df_num.describe())
