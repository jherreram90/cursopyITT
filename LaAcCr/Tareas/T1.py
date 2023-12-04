a=input('ingrese 1er materia: ')
a1=float(input('calificacion:'))
print('\n')
b=input('ingrese 2da materia: ')
b1=float(input('calificacion:'))
print('\n')
c=input('ingrese 3ra materia: ')
c1=float(input('calificacion:'))
print('\n')
d=input('ingrese 4ta materia: ')
d1=float(input('calificacion:'))
print('\n')
e=input('ingrese 5ta materia: ')
e1=float(input('calificacion:'))
print('\n')
f=input('ingrese 6ta materia: ')
f1=float(input('calificacion:'))
print('\n')
l1=(a,b,c,d,e,f)
l2=(a1,b1,c1,d1,e1,f1)
#print("\n".join(map(str, l1)))

l3=list(zip(l1,l2))
l4=dict(zip(l1,l2))
print('lista de tuplas:','\n',l3,"\n")
print('Diccionario: \n',l4,"\n")

for x,y in l4.items():
	print(x,': ',y)

suma=a1+b1+c1+d1+e1+f1
promedio=suma/6
print("El promedio es: ",promedio)

