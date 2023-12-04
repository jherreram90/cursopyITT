'''op = 'uno'
match op:
    case 'uno':
        print('opcion 1')
    case 'dos':
        print('opcion 2')
    case 'tres':
        print('opcion 3')
        
'''
import random as rd

edades = []

for i in range(0,35,1):
    edades.append(rd.randint(1,100))
    for i in edades:
        if i <= 17:
            print (f'{i} es menor de edad')
        elif i >= 18 and i <= 45:
            print (f'{i} es mayor de edad')
        elif i >= 46 and i <= 100:
            print (f'{i} es de tercera edad')

#OTRA FORMA DE RESOLVERLO

print (rd.randint(0,95))