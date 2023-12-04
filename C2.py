#objetos iterables mediante ciclos while y do while
#tuplas
#listas
#diccionarios
#listas de listas(matrices)
#listas de listas de listas(hipermatrices)
#complejidad el tiempo de ejecucion que tardas en realizar una tarea.
#complejidad lineal,cuadratica,polinomica(exponencial), logaritmica.

#l1=[1,2,3,4,5,'hola mundo',0.5,'44',[11,12,13,14,15],(4,2)]

#iteracion
#bucle
"""for i in l1:
	print(type(i))
for i in range(len(l1)):
	print(l1[i])"""

#range(min, max) es una funcion que devuelve un iterable, entre min y max=, no es necesario especificar el minimo
#pero si el maximo
#len(arr)es una funcion que permite conocer el tamaño de un arreglo.

'''print(l1[0:5])
print(l1[8][1:4])
print(l1[9][1])
print(l1[5][5:10])'''

#diccionarios
l1=[1,2,3,4,5,'hola mundo',0.5,'44',[11,12,13,14,15],(4,22)]
d1={'Nombre':'Jorge','Apellido':'Herrera','Dpto':'Siscom'}
#print(d1)

#iterando sobre keys...sobre llaves
'''for i in d1:
	#print(i)

	#se obtienen unicamente los valores
	print(d1[i]) 

for x,y in d1.items():
	print(x,': ' ,y)'''

#print(d1.get('Nombre'))
"""print(d1.keys())
print(d1.values())
"""
"""d1.pop('Nombre')
print(d1)

print(l1.pop())
print(l1)"""

l2=[1,2,3,4,5]
l3=['hola mundo',0.5,'44',[11,12,13,14,15]]
"""
print(l2)
l2.append('hola mundo')
print(l2)

print(l2)
l2.extend(l3)
print(l2)"""
"""
print(l2)
l2.insert(2,'hola')
l2.insert(4,'hola')
l2.insert(4,'hola')
print(l2)

print(l2.index('hola'))
print(l2.count('hola'))
"""

#lista de tuplas
"""
l3=[('Nom:','Jorge'),('Apell:','herrera'), ('Dpto','Siscom')]
d=dict(l3)
print(d)
listas de tuplasa apartir de una independiente
""" 
l4=['POO', 'POE', 'MVC']
l5=[70,80,90]
#l6=zip(l4,l5)
#lista o diccionarios con dict

l7=list(zip(l4,l5)) #tuplas
l8=dict(zip(l4,l5))#diccionario

print(l7)
print(l8)

