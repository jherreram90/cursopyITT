print ()
# condicionales

"""
									IF NORMALITO
a = 1
b = 2

c = 'hola'
d = 'hola'

if a != b:
	print ('no son iguales')
else:
	print ('si son iguales')

if d != c:
	print ('no son iguales')
else:
	print ('si son iguales')
"""
"""
chico_tienda = True

if chico_tienda:
	print ('si vino el chico_tienda')
else:
	print ('no vino :( ')
"""
"""
 							EL USO DE ELIF
a, b, c = 13, 22, 80

if 0<a<17:
	print('es un niño')
elif 18<a<45:
	print ('es un adulto')
else:
	print('es un anciano')
# comparando B
if 0<b<17:
	print('es un niño')
elif 18<b<45:
	print ('es un adulto')
else:
	print('es un anciano')
# comparando C
if 0<c<17:
	print('es un niño')
elif 18<c<45:
	print ('es un adulto')
else:
	print('es un anciano')
"""
"""
									MATCH 

op = 'dos'
match op:
	case 'uno':
		print ('opcion 1')
	case 'dos':
		print ('opcion 2')
	case 'tres':
		print ('opcion 3')
"""

"""
import random as edad

a = [] # guarda edades
b = [] # guarda niños
c = [] # guarda jvenes
d = [] # guarda adultos
e = [] # guarda ancianos

# interable con range 
for i in range(34):
	# append añade las edades en a
	a.append(edad.randint(0,95))

print (a)

for i in a:
	if   0 < i < 17:
		b.append(i)
	elif 18 < i < 45:
		c.append(i)
	else:
		d.append(i)

print('\n EDADES DE NIÑOS: ', b, '\n TOTAL DE NIÑOS: ', len(b),
	  '\n EDADES DE ADOLESCENTES: ', c, '\n TOTAL DE ADOLESCENTES', len(c),
	  '\n EDADES DE ANCIANOS: ', d,'\n TOTAL DE ANCIANOS', len(d))
"""

# 100 edades
# crear una cuenta en git 



import random as edad

a = [] # guarda edades
b = [] # guarda niños
c = [] # guarda jvenes
d = [] # guarda adultos
e = [] # guarda ancianos


for j in range(100):
	# append añade las edades en a
	a.append(edad.randint(0,95))


print (a)

for j in a:
	if 0 >= j <= 12:
		b.append(j)
	elif 13 >= j <= 18:
		c.append(j)
	elif 19 >= j <= 60:
		d.append(j)
	else:
		e.append(j)

print('\n EDADES DE NIÑOS: ', b, '\n TOTAL DE NIÑOS: ', len(b),
	  '\n EDADES DE ADOLESCENTES: ', c, '\n TOTAL DE ADOLESCENTES', len(c),
	  '\n EDADES DE ADULTOS: ', d, '\n TOTAL DE ADULTOS', len(d),
	  '\n EDADES DE ANCIANOS: ', e,'\n TOTAL DE ANCIANOS', len(e))



