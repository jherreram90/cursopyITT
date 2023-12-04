#Listas
l1=['a', 'b', 'c', 1, 2, 3.5, 'holi c:', True, False]

#print(type(l1))

#print(l1[0])

#SLICES: fraciones o fragmentos de una lista

#print(l1[3:6])

#para hacer operaciones dentro de una lista
#promedio
#print(sum(l1[3:6])/4)

#promedio a partir de la longitud de la lista
#print(f"Primedio de numeros",sum(l1[3:6])/len(l1[3:6]))

#iteracion dentro de una lista

'''for elemento in l1:
    print(elemento)

print("")

#tambien de puede definir de un punto a otro punto
for i in range (len(l1[3:6])):
    print(l1[i])
    
print("") 

for i in range (3,len(l1)):
    print(type(l1[i]))
    
print("")

#Iterar dentro de un elemento de una lista "hola"="ho"
print(l1[6][0:2])'''

l2=[['Lopez', 'Hernandez', 'Joel', 'Carlos', '10/02/1982'],
    ['Dominguez', 'Andrade', 'Angel', 'Giovanni', '16/02/1999'],
    ['Ruiz', 'Cadena', 'Adamaris', 'Yazmin', '11/06/2000'],
    ['Reyes', 'Moncevais', 'Guadalupe', 'Cristel', '17/12/1999'],
    ['Lucio', 'Lopez', 'Paola', 'Montserrat', '16/04/1999']] #'ASDFJUed3'
'''
Problematica.
Identificar si hay dos nombres de pila
Generar clave unica de 9 elementos 
Generar curp con slices
Hacer todo para 5 personas
'''

#IDENTIFICAR SI HAY DOS NOMBRES

#Generar clave unica de 9 elementos

#se va a hacer igual que el de abajo c:

#Generar CURP con SLICES

for sublista in l2:
    primer_elemento = sublista[0]
    #ahora sublista tiene los nuevo elementos
    for letra in primer_elemento:
        primer_letra = primer_elemento[0:2]
        
    segundo_elemento = sublista[1]
    for letra2 in segundo_elemento:
        segunda_letra = segundo_elemento[0:2]
        
    tercer_elemento = sublista[2]
    for letra3 in tercer_elemento:
        tercer_letra = tercer_elemento[0:2]
    
    cuarto_elemento = sublista[3]
    for letra4 in cuarto_elemento:
        cuarta_letra = cuarto_elemento[0:2]
        
    quinto_elemento = sublista[4]
    for letra5 in quinto_elemento:
        fecha1 = quinto_elemento[0:2]
        fecha2 = quinto_elemento[3:5]
        fecha3 = quinto_elemento[6:7]
        
    print(f"{primer_letra}{segunda_letra}{tercer_letra}{cuarta_letra}{letra5}{fecha1}{fecha2}{fecha3}")


'''
for sublista in lista_de_listas:
        primer_elemento = sublista[0]
        segundo_elemento = sublista[1]
        print(f"Primer elemento: {primer_elemento}, Segundo elemento: {segundo_elemento}")
'''