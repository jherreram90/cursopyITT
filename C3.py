"""a=1
b=2
c=('hola')
d=('Hola')

if a!=b:
	print('no son iguales')
else:
	print('si son iguales')"""


"""Chico_tienda=False

if Chico_tienda:
	print('Si vino el chico tienda')
else:
	print('No vino :(')"""

"""a,b,c=10,22,80

if 0<c<17:
	print('Es un niñe......')
elif 18<c<45:
	print('Es un adulto........')
else:
	print('Es un anciano....')"""

#match y elif, 

"""op='uno'
match op:
	case 'uno':
		print('opcion 1')
	case 'dos':
		print('opcion 2')
	case 'tres':
		print('opcion 3')"""


"""lst1[edad1,edad2,...,edad35]

itera sobre lst1
imprime arreglo de 0<lst1[i]<17
imprime arreglo de 18<lst[i]<45
imprime arreglo de lst1[i]>45
hint:usa randrange()
hint2:import random
random.randint(x,y)"""

import random as rd

lst1=[]
b=[]
c=[]
d=[]


lst1=[random.randint(0,95)
for i in range (34)]
print(lst1)

if 0<c<17:
	print('Es un niñe......')
elif 18<c<45:
	print('Es un adulto........')
else:
	print('Es un anciano....')"""