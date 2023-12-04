li =[1,2,3,4,5,'hola mundo',0.5,'44',[11,12,13,14,15],(4,22)]
'''
tuplas
listas
listas de listas (matrices)
listas de listas de listas (hipermatrices)
diccionarios
'''

'''for i in li:
    print(type(i))
    
for i in range(len(li)):
    print(li[i])'''

'''
range (min, max) es una funcion que devuelve un iterable, entre
min y max, no es necesario especificar el minimo pero si el max
len(arr) es una funcion que permite conocer el tamaño del arreglo
'''
'''print (li[0:5])

print(li[8][1:4])

print(li[9][1])

print(li[5][5:10])'''

#DICCIONARIOS

diccionario = {
    'Nombre':'Gabriel',
    'Apellido':'Dominguez',
    'Dpto':'Becario'
}

'''print(diccionario)

#ITERANDO SOBRE KEYS
for i in diccionario:
    #para llaves
    print(i)
    #para valores
    print(diccionario[i]) 

for x,y in diccionario.items():
    print(x,':',y)'''
    
'''print (diccionario.get('Nombre'))
print(diccionario.keys())
print(diccionario.values())

#quitar/eliminar key y value
diccionario.pop('Nombre')
print(diccionario)'''

'''print(li)
print(li.pop())
print(li)'''

l2=[1,2,3,4,5]
#l3=('hola mundo',0.5,'44',[11,12,13,14,15],(4,22))

'''print(l2)
l2.append('hola mundo')
print(l2)
l2.extend(l3)
print(l2)'''

l2.insert(2,'hola mundo')
l2.insert(3,'hola mundo')
l2.insert(4,'hola')
l2.insert(5,'hola')
print(l2)

#Preguntar el indice en donde se encuentra un objeto
print(l2.index('hola mundo')) #retorna el primero que encuentra

print(l2.count('hola')) #cuenta cuantos hay

'''l3=[('Nombre:''Gabriel'),
    ('Apellido:''Dominguez'),
    ('Dpto:''Becario')]
d=dict(l3)
print(d)'''

l4=['POO', 'POE', 'MVC']
l5=[70,80,90]
#l6=zip(l4,l5)
l7=list(zip(l4,l5))
l8=list(zip(l4,l5))
print(l7)
print(l8)

'''
Recinbir 6 nombre de materias por teclado y sus calificaciones (int/float)
-IMPRIMIR LISTA DE TUPLAS
-IMPRIMIR DICCIONARIO
-ITERAR SOBRE X,Y EN DICCIONARIO PARA HACER UNA IMPRESION VERTICAL
-IMPRIMIR PROMEDIO
'''