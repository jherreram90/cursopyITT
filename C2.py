
"""
									09/10/2023

las iteraciones son importantes 
->tuplas 
->listas 
->diccionarios 
->listas de listas (matrices)
->listas de listas de listas (hipermatrices)

complejidad al tiempo de ejecucion de una tarea o un algoritmo
"""

l1=[1,2,3,4,5, 'hola world', 0.5, '44', [11,12,13,14,15],(4,22)]

# for 1
for i in l1:
	print(i)

for i in l1:
	print(type(i))

"""

l1[item, item, item]
	0 	  1 	2

"""

# for 2

"""

range (max, min)es una funcion que devuelve un iterable
min y max, no es necesario especificar el minimo pero si el
maximo
len (arr) es una funcion que permite conocer el tamaño del 
arreglo

"""
for i in range (len(l1)):
	print (l1[i])

"""

REBANADAS 

"""
# primero elementos 
print (l1[0:5])
# acceder a una sublista
print (l1[8])
# accder a una sub lista y el rango de elemtos a contemplar
print (l1[8][1:4])
# accder a un elemento de una tupla 
print (l1[9][1])
# acceder a un elemto de una lista (los str son iterable)
print (l1[5][5:10])


# 						DICCIONARIOS

d1 = {
	'nombre':'jorge',
	'apellido':'herrera',
	'depto':'sistemas'
}
print (d1)

# iterando sobre keys

for i in d1:
	#valores
	print(i)
	# llave valor
	print (d1[i])

# 

for x,y in d1.items():
	print(x, ': ', y)

print (d1.get('nombre'))
print (d1.keys())
print (d1.values())


d1.pop('nombre')
print (d1)




print(l1.pop())
print (l1)


l2 = [1,2,3,4,5]
l3 = [('nom: ','Gael'),('Apellido: ','Hernandez'),('Depto: ','ISC')]

l2.append( 'hola wordl' )
print(l2)

print(l2)
# l2.extend(l3)
print(l2)

l2.insert(2, 'hi wordl')
print(l2)
# solo retorna el primer valor encontrado
print(l2.index('hola wordl'))

l2.insert(2, 'hi')
l2.insert(4, 'hi')
l2.insert(5, 'hi')

print(l2.count('hi'))


d=dict(l3)
print (d)



l4 = ['POP ', 'POE ', 'MVC ']
l5 = [70, 80, 90]
l6 = zip(l4,l5)
print (list(l6))
l7 = list(zip(l4,l5))
l8 = dict(zip(l4,l5))

print(l7)
print(l8)



git 

branch 















