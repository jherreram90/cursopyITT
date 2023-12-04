
"""
def sum(*args):
	
	suma=0
	for i in args:
		suma+=i
	return suma

print(sum(3,2,1))
"""
"""
def suma(*args):
    s = 0
    for arg in args:
        s += arg
    return s

print(suma(1, 3, 4, 2))
#Salida 10

print(suma(6, 3))
#Salida 9
"""
#-----------------------------------------------------------------
"""
import math
def cajero(acciones, *args):
	if consultar == "consulta":

	elif retiro == "retiro":

	elif insercion == "insercion"

	return tarjeta_retirada
"""
"""
def saldo(L):
    
    S=50+L
    return  print('El saldo total es de: ', S)

def retiro(R):

    r=50-b
    return print('El saldo total es de ', r)
"""

def cajero(*args):
    if args == saldo(L):
    	L=args[0]
    	S=50+L
    	return  print('El saldo total es de: ', S)
    elif accion == retiro(b):
    	b=args[0]
    	r=50-b
    	return print('El saldo total es de ', r)

print("Cajero automatico.\n")
print("1.insertar.\n2.Retirar.")
x=int(input("Escoje la accion a realizar: "))

if x==1:
    L=int(input('Ingrese el saldo: '))
    saldo(L)
  
if x==2:
    
    b=int(input('Ingrese dinero a retirar: '))
    retiro(b)
