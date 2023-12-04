import random as rd

a=[]
b=[]
c=[]
d=[]
e=[]
rd.randint(0,80)

for i in range(100):
	a.append(rd.randint(0,80))
#append => se utiliza para agregar a la lista 

print(a,'\n')

for x in a:
	if 0<x<12:#niños
		b.append(x)
	elif 13<x<18:#adolecentes
		c.append(x)
	elif 19<x<60:#adultos
		d.append(x)
	else:#ancianos
		e.append(x)

print('Niños: ',len(b),'\nEdades:',b, 
	'\nAdolecentes ',len(c), '\nEdades:',c, 
	'\nAdultos:',len(d), '\nEdades:',d, 
	'\nAncianos:',len(e), '\nEdades:',e)

l1=(b)
l4=dict(zip(l1))
print('Diccionario: \n',l4,"\n")