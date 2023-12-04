
#l1=[1,2,3,4,5,'hola mundo',0.5,'44',[11,12,13,14,15],(4,22)]

#for i in l1:
	#print(i)#imprime la cadena 1x1
	#print(type(i))#imprime el tipo que pertence cada caracter 

#for i in range(len(l1)):
	#print(l1[i])

"""range(min, max) es una funcion que deveulve un iterable, entre
min y max, no es necesario especificar el minimo pero si el max,
len(arr) es una funcion que permite conocer el tamaño de un reglon"""

"""print(l1[0:5])
print(l1[8][1:4])
print(l1[9][1])
print(l1[5][5:10])"""

"""------------------------DICCIONARIOS---------------------------"""
"""l1=[1,2,3,4,5,'hola mundo',0.5,'44',[11,12,13,14,15],(4,22)]

d1={'Nombre':'Cris', 'Apellido':'Weir', 'Carrera':'Sistem. Computa.'}
#print(d1)
for i in d1:
	print(i)#imprime sonre las llaves todo lo que se encuentre dentro de ellas
	print(d1[i])#imprime solo los valores que  tienen los diccionarios

#for x,y in d1.items():
#	print(x,': ',y)#separa los valores de las llaves"""

#print(d1.get('Nombre)#imprime el valor dentro de la llave
#print(d1.keys())#imprime las llaves
#print(d1.values())#imprime los valores de las llaves

#d1.pop('Nombre')#imprime todos los valores menos el mencionado de la llave
#print(d1)

#print(l1.pop())#imprime el valor entre parentesis
#print(l1) 
"""-------------------------------------------------------"""
#l2=[1,2,3,4,5]
#l3=['hola mundo',0.5,'44',[11,12,13,14,15]]

"""print(l2)
l2.append('Hola mundo ')#se agrega a la lista que ya se tenia
print(l2)

print(l2)
l2.extend(l3)#se conectan las listas 
print (l2)"""

"""print(l2)
l2.insert(2, 'Hola')#inserto la palabra en la posicion 2 de la cadena 
l2.insert(4, 'Hola')
l2.insert(4, 'Hola')
print (l2)

print(l2.index('Hola'))#sirve para buscar en que posicion se encuentra el caracter a buscar
print(l2.count('Hola'))#sirve para contar el numero del caracter que se quiere contar
"""

"""---------------------------------------------------------------------------"""
l3=[('Nombre:','Cris'),('Apellido:','Weir'), ('Carrera:','Sistem. Computa.')]
#d=dict(l3)
#print(d)

l4=['POO','POE','MVC']
l5=[70,80,90]
#print(l4)
#print(l5)
l6=zip(l4,l5)#junta las dos listas
print(list(l6))#imprime a manera de lista
l7=list(zip(l4,l5))#los convirtio en una lista de tuplas
l8=dict(zip(l4,l5))#los convirtio en un diccionario
print(l7)
print(l8)





