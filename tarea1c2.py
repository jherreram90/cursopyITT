
l4= input("Ingrese el nombre de 6 materias: ")
print("ingrese las calificaciones")
l5= float(input('Ingrese las 6 calificaciones: '))
cal=[]
nom=[]
#i=0
#n=6
nom.append(l4)
cal.append(l5)

"""while i <n:
   num=float(input("Ingresa las calificaiones de las materias: "))
   cal.append(num)
   i+=1"""

print(nom)  #IMPRIME LISTAS
print(cal)  
print()
l7=list(zip(nom,cal))# ZP JUNTA LAS LISTAS l4 y l5 y LIST convierte en una lista de tuplas
l8=dict(zip(nom,cal))#los convirtio en un diccionario
print(l7)
print()
print(l8)
print()
for x,y in l8.items():
	print(x,', ',y)#separa los valores de las llaves

print()
prom = sum(cal[0:])/len(cal[0:])
print('El promedio es: ', prom)

materias=[]
calificaciones=[]
for x in range(6):
    mat=input("Ingrese el nombre de la materia:")
    materias.append(mat)
    cal1=int(input("Ingrese la calificacion:"))
    calificaciones.append(cal1)

for x in range(6):
    print(materias[x],calificaciones[x])

prom=sum(calificaciones[0:])/len(calificaciones[0:])
print('El promedio es: ', prom)