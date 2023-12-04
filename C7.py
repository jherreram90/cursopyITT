class Tarjeta(object):
    """docstring for Tarjeta"""
    def __init__(self, serie, deposito_inicial, retiro_inicial, saldo_inicial):
        self.seri = serie
        self.depo = deposito_inicial
        self.reti = retiro_inicial
        self.sald = saldo_inicial

    def deposito(self, deposito):
        self.sald = self.depo + self.sald
        print('Depositaste:', self.depo, 'Saldo actual:', self.sald)

    def retira(self):
        self.sald = self.sald - self.reti
        print('Retiraste:', self.reti, 'Saldo actual:', self.sald)

t1 = Tarjeta('5671234', 300, 50, 254312)
t1.deposito(200)
t1.retira()

t2 = Tarjeta('8976541', 100, 150, 5300)
print('La serie de la tarjeta 2 es:', t2.seri)
print('El saldo de la tarjeta es:', t2.sald)
