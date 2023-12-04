# args para metro especial para una funcion 

"""
def sum(*args):

	suma = 0
	for i in args:
		suma += i
	return suma

print (sum(3,2,1))

help(sum)

"""

																# CAJERO 
# RETIRAR 
# DEPOSITAR 
# CHCAR SALDO 

def cajero(*args):
	saldo = 0
	for movimiento in args:
		if movimiento > 0:
			saldo += movimiento
		elif movimiento < 0:
			if abs(movimiento) <= saldo:
				saldo -= movimiento
	return saldo



sal_dep = cajero (200, 500, 125, 230)
retiro = 100 + 150 + 50 
sal_ret = cajero (sal_dep - retiro)
saldo = sal_dep - retiro
print ("saldo depositado: " + str(sal_dep))
print ("saldo retirado: " + str(retiro))
print ("saldo actual: " + str(saldo))

