"""basico"""
#! operadores, variables
#hello = 'tim'  
#name= input('name: ')
#print('hello', name)

x=3
y=4
potencia= 5 **3  # potencia
division_integer= 10//3 #* da el integer de la division, sin decimales, devuelve 3
remainder= 1%3 # da 1 el residuo
result=x/y #da un float de resultado
result2= int("4") # da integer de un string

#! metodos en strings

hello= 'hello'.upper()

count= 'sadfsdg'.count('s')# da el numero de aariciones de algo en un string

condiciones= (4 > 5 ) or ((1>2) and (5 <10)) or not(1>5)

#! condicionales

if x== 'tim':
   algo='verdad'
   otro= 'asdsd'
elif x=='asdasd':
   algo= 'elif'
else: algo='falso'

#! listas

x = [4 ,'sad',True]
x.append('añade elemento') # añade elemento a x
x.extend(['array','cosas']) # AGREGA UN ARRAY A UN ARRAY
ultimo_elemento=x.pop()  # da el ultimo elemento  lo elimina del array
x[0]  = 'nuevo1'
largo = len(x) # da el length de alfo

#hace la seleccion en un array, con inico gin, paso
sliced = x[0:3:1] #inicio, fin, pasos

#* topples son como listas, pero son TOTALMENTE inmutables
topple= (0, 'inmutable', 5)


#! for
a=1
for i in range(10): # imprime de cero a nueve
   a=a+1
for i in range(1,10,2): # for inicia en 1, acaba en 9, y va en pasos de 2
  # print(i) # da 1 , 3 ,5 ,7 ,9 
  a=a+1

i=1
array=[3,5,7] 
for i in array:# los recorre
  # print(i) # da 1 , 3 ,5 ,7 ,9 
   if i == 5:# todo for en python es for each
      break

#! while

i=0
while (i<10):
   i +=1

#! SETS
x=(5,7,8,5)
s = set(x)
s.add(5)
s.remove(5)
esta= 5 in s#saber si un obheto esta en algo # da False
s2= {5,7,8,6,5,135,'asd',6} #* forma de definir sets con datos de una vez, no se puede dejar vacio o hace un diccionario

nuevo_set= s.union(s2) #*une dos sets
nuevo_set2= s.difference(s2) #*da las diferencias de dos sets
nuevo_set3= s.intersection(s2) #* da la interseccion de sets

#! diccionarios como un MAP en javascript

map= {'key':4}
map['key2']=5
map[2]=[5,7,8]
buscar= 5 in map  # busca en los keys
values= list(map.values())
keys= list(map.keys())

for key, value in map.items(): #iterar en un map
   #print(key, value)
   a=1


#! funciones
def func(arg):
   #print(arg)
   return arg*5

func(3)

#* funciones con * ,, ** para diccionarios

def func_map(a,b):
   #print(a,b)
   a=1

func_map(**{'b':5,'a':3}) #*funcion busca los argumentos con el nombre en el map

func_map(*[(1,2),(3,5)]) #*da cada elemento separado como argumento



#! errores, excepciones

#raise Exception('bad') # como un throw Error en javascript

try:
   x=7/0
except Exception as e: # si hay error pasa aca
   a=1
finally: # lo corre haya error o no
   a=1

#! map function hacer filtros o hacer funcione sobre arrys

x=[1,2,5,3,6,4,7,8,9,6] # lambda es una funcion de una sola linea
mp= map( lambda i: i+2, x)#* realiza una funcion sobre un attay a recorrer

#filtra elementos
filtro = filter( lambda i: i % 2 == 0, x) #*devuelve todo lo divisivle por 2

def func(i):
   return i % 2 == 0
filtro = filter( func, x) #mismo filtro pero con una funcion normal


print()
