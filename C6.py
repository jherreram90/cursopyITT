class Tarjeta(object):
	"""docstring for Tarjeta"""
	def __init__(self, serie, deposito, retiro, saldo):
		self.seri=serie
		self.depo=deposito
		self.reti=retiro
		self.sald=saldo

	def deposito(self):
		saldo=self.depo+self.sald
		print('Depositaste: ', self.depo, 'Saldo actual: ', saldo)

	def retira(self):
		saldo=self.sald-self.reti
		print('Retiraste: ', self.reti, 'Saldo actual: ', saldo)
		
t1=Tarjeta('5671234', 300, 50, 254312)
t1.deposito()
t1.retira()

t2=Tarjeta('8976541',100,150,5300)
print('La serie de la tarjeta 2 es:', t2.seri)
print('El saldo de la tarjeta 2 es:', t2.sald)


#Solo instanciar con serie y saldo
#Verificar si es tarjeta bancaria, si lo es
""" *Solicitar NIP
*Solicitar CVV
*Solicitar fecha (date)
****Enviar aviso si esta cerca la fecha de expiración con un metodo 
#Si no es tarjeta bancaria, unicamente solicitar saldo y serie.
#Ambos casos: Se define el monto de depósito y retiro desde las funciones correspondientes.
#instanciar con for
2 tarjetas bancarias
2 tarjetas no bancarias"""

class Tarjetas(object):
	"""docstring for Trajetas"""
	def __init__(self, saldo, serie, nip, cvv, fecha):
		self.sal=saldo
		self.ser= serie
		self.np=none
		self.cv=none 
		self.fech=none

	def tarjeta_banco (self):
		return True

tarjeta=Tarjetas('2132384662187321')




