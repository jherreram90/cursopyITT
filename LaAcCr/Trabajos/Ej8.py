"""class Tarjeta(object):
	def __init__(self, serie, deposito, retiro, saldo):  #self es un apuntador
		self.seri=serie
		self.depo=deposito
		self.reti=retiro
		self.sald=saldo

	def deposito(self):
		saldo=self.depo+self.sald
		print('Depositaste: ',self.depo, 'Saldo actual: ',saldo)


	def retira(self):
		saldo=self.sald-self.reti
		print('Retiraste: ',self.reti, 'Saldo actual: ',saldo)		

t1=Tarjeta('5671234', 300, 50, 254312)
t1.deposito()
t1.retira()

t2=Tarjeta('8976541', 100, 150, 5300)
print('La serie de la tarjeta 2 es: ', t2.seri)
print('El saldo de la tarjeta 2 es: ', t2.sald)"""

from datetime import datetime

class Tarjeta(object):
    def __init__(self, serie, saldo, es_bancaria=False):
        self.serie = serie
        self.saldo = saldo
        self.es_bancaria = es_bancaria

        if self.es_bancaria:
            self.nip = input('Ingrese NIP: ')
            self.cvv = input('Ingrese CVV: ')
            fecha_expiracion_str = input('Ingrese la fecha de expiración (formato MM/YYYY): ')
            self.fecha_expiracion = datetime.strptime(fecha_expiracion_str, '%m/%Y')

    def deposito(self, monto):
        if self.es_bancaria:
            self.verificar_tarjeta()
        self.saldo += monto
        print('Depositaste:', monto, 'Saldo actual:', self.saldo)

    def retira(self, monto):
        if self.es_bancaria:
            self.verificar_tarjeta()
        if monto <= self.saldo:
            self.saldo -= monto
            print('Retiraste:', monto, 'Saldo actual:', self.saldo)
        else:
            print('Saldo insuficiente. No se puede realizar el retiro.')

    def verificar_tarjeta(self):
        if self.es_cerca_expiracion():
            print('¡Atención! La tarjeta está cerca de su fecha de expiración.')

    def es_cerca_expiracion(self):
        if self.es_bancaria and (self.fecha_expiracion - datetime.now()).days <= 30:
            return True
        return False

# Instancias con dos tarjetas bancarias y dos no bancarias
t1 = Tarjeta('5671234', 254312, es_bancaria=True)
t2 = Tarjeta('8976541', 5300, es_bancaria=True)
t3 = Tarjeta('11112222', 10000)
t4 = Tarjeta('33334444', 5000)

# Ejemplos de depósito y retiro
t1.deposito(300)
t1.retira(50)

t2.deposito(100)
t2.retira(150)

t3.deposito(2000)
t3.retira(500)

t4.deposito(1000)
t4.retira(200)