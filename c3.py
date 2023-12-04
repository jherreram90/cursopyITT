"""a=1
b=2
c='hola'
d='Hola'
if a!=b:
 	print('No son iguales')
else:
 	print('Si son iguales')

Chico_tienda=False
if Chico_tienda:
    print('Si vino el chico tienda')
else:
	print('No vino :(')
    """

"""a,b,c = 10,22,80 

if 0<b<17:
    print('es un  niñe...')

elif 18<b<45:
    print('Es un adulto...')

else:
    print('Es un anciano...')

 #Similar a switch"""

"""
op='dos'

match op:
    case 'uno':
        print('opcion 1')
    case 'dos':
        print('opcion 2')
    case 'tres':
        print('opcion 3')"""

import random as rd
print(rd.randint(0,95))

a=[]
b=[]
c=[]
d=[]

for i in range(34):
	a.append(rd.randint(0,95))

print(a)

for i in a:
	if 0<i<17:
		b.append(i)
	elif 18<i<45:
		c.append(i)
	else:
		d.append(i)

print('Niños: ',len(b), '\nEdades:' ,b, '\nAdolescentes: ', len(c),'\nEdades:'  ,c, '\nAdultos', len(d), '\nEdades: ' ,d)