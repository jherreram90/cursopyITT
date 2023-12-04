"""
a=1
b=2
c='Hola'
d='hola'

#if a==b comparadores
#if a!=b comparadores
if d!=c:
	print('no son iguales')
else:
	print('Son iguales')

"""

"""
#chico_tienda=True
chico_tienda=False

if chico_tienda:
	print('Esta aqui')
else:
	print('no vino 7n7')

"""
#--------------comparadores---------
"""
a, b, c =10,22,80

if 0<c<17:
	print('Is a boy')
elif 18<c<45:
	print('Es adulto')
else:
	print('Es un anciano')
"""
#-----------------sentencia match----------
"""
op =1
match op:
	case 1:
		print('opcion 1')
	case 2:
		print('opcion 2')
	case 3:
		print('opcion 3')"""
"""
op ='Hola'
match op:
	case 'hola':
		print('opcion 1')
	case 'Hola':
		print('opcion 2')
	case 'adios':
		print('opcion 3')"""

#--------------------------------------------

import random as rd

a=[]
b=[]
c=[]
d=[]

rd.randint(0,95)

for i in range(34):
	a.append(rd.randint(0,95))
#append => se utiliza para agregar a la lista 

print(a,'\n')

for x in a:
	if 0<x<17:
		b.append(x)
	elif 18<x<45:
		c.append(x)
	else:
		d.append(x)

print('Niños: ',len(b),'\nEdades:',b, 
	'\nAdolecentes ',len(c), '\nEdades:',c, 
	'\nAdultos:',len(d), '\nEdades:',d)