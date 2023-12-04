"""
def suma1(a,b):
	c = a+b
	return c

a = int(input('Ingresa a: '))
b = int(input('Ingresa b: '))

c = suma1(a, b)  
print(c)

"""
"""
list1 = ['niños', 'adolescentes', 'adultos']
funcion 1 genera un diccionario
# crea un diccionario con las edades aleatorias 
def dic1(list1, n): #n edades aleatorias 
	return dic
# 
dic2 = {'niños: ', []
		'adolescentes: ', []
		'adultos', []}

def pequeños (dic1):
	return arreglo_niño_pequeños 
"""

import random
import math

"""
n = [random.randint(0, 100) for _ in range(100)]

list1 = [
    'niños', [edad for edad in n if 0 <= edad <= 12 ],
    'adolescentes', [edad for edad in n if 13 <= edad <= 18],
    'adultos', [edad for edad in n if 19 <= edad <= 60]
]

#print (list1)

def diccionario(list1, n):
	d1 = {'niños':n,
	'adolescentes':n,
	'adultos':n}
	dic = list1, n
	return dic

c = diccionario(list1, n)
print (c)


def pequeños(diccionario):
	a = [] #guardamos las edades 
	b = [] #guardamos niños

	for j in pequeños:
		if 0<= j <= 12:
			b.apeend(j)
			peque = pequeños
			return peque

d = pequeños(diccionario)
print (d)
"""

"""
figura = input('Que figura quieres sacar: \nc: circulo \nt: triangulo \ns: cuadrado \n' )
dat1 = float(input('ingresa dato1: '))
dat2 = float(input('ingresa dato2: '))

def area1(dat1, dat2):
	op = match (dat1, dat2):
		case (1, 'c'):
			PI = math.pi
			dat2 = false
			area = PI*dat1*dat1
			print ('area del circulo')
		case 't':
			print ('area del triangulo')
		case 's':
			print ('area del cuadrado')
		case 'h':
			print ('area del ')
	return op

print (area1(1, 'c'))

#are = area1(dat1, dat2)
#print (are)

"""

import math

def calcular_area(tipo_figura, *args):
	if tipo_figura == "triangulo":
		base, altura = args
		return 0.5 * base * altura
	elif tipo_figura == "cuadrado":
		lado = args[0]
		return lado * lado
	elif tipo_figura == "rectangulo":
		base, altura = args
		return base * altura
	elif tipo_figura == "circulo":
		radio = args [0]
		return math.pi * radio * radio
	else:
		return "figura no valida"



print ("Área del rectangulo: ", calcular_area("rectangulo", 8, 3))
print ("area del triangulo: ", calcular_area("triangulo", 6, 4))
print ("area del cuadrado: ", calcular_area("cuadrado", 5))
print ("area del circulo: ", calcular_area("circulo", 5))



