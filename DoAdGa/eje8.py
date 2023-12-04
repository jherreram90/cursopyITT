class Tarjeta(object):
    """docstring for Tarjeta"""
    def __init__(self, serie, deposito, retiro, saldo):
        self.seri = serie
        self.depo = deposito
        self.reti = retiro
        self.sald = saldo

    def depositar(self):
        saldo = self.depo + self.sald
        print('Depositaste:', self.depo, 'Saldo actual:', saldo)

    def retirar(self):
        saldo = self.sald - self.reti
        print('Retiraste:', self.reti, 'Saldo actual:', saldo)

t1 = Tarjeta('5671234', 300, 50, 254312)
t1.depositar()
t1.retirar()

t2 = Tarjeta('8976541', 100, 150, 5300)
print('La serie de la tarjeta 2 es:', t2.seri)
print('El saldo de la tarjeta 2 es:', t2.sald)
