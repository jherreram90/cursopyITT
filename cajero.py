class Tarjeta:
    def __init__(self, serie, saldo):
        self.serie = serie
        self.saldo = saldo

    def solicitar_nip(self):
        return input("Ingrese su NIP: ")

    def solicitar_cvv(self):
        return input("Ingrese su CVV: ")

    def solicitar_fecha_expiracion(self):
        fecha_str = input("Ingrese la fecha de expiración (MM/YY): ")
        return fecha_str

    def esta_cerca_expiracion(self):
        fecha_expiracion = self.solicitar_fecha_expiracion()
        hoy = self.obtener_fecha_actual_str()
        proximo_mes = self.sumar_mes_a_fecha(hoy)
        return fecha_expiracion < proximo_mes

    def obtener_fecha_actual_str(self):
        # Devuelve la fecha actual en formato MM/YY
        return input("Ingrese la fecha actual (MM/YY): ")

    def sumar_mes_a_fecha(self, fecha_str):
        # Suma un mes a la fecha ingresada y devuelve el resultado en formato MM/YY
        mes, anio = map(int, fecha_str.split('/'))
        mes += 1
        if mes > 12:
            mes = 1
            anio += 1
        return f"{mes:02d}/{anio:02d}"

class TarjetaBancaria(Tarjeta):
    def __init__(self, serie, saldo):
        super().__init__(serie, saldo)

    def depositar(self, monto):
        self.saldo += monto
        print(f"Depósito de ${monto} realizado. Nuevo saldo: ${self.saldo}")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de ${monto} realizado. Nuevo saldo: ${self.saldo}")
        else:
            print("Saldo insuficiente.")

class TarjetaNoBancaria(Tarjeta):
    def __init__(self, serie, saldo):
        super().__init__(serie, saldo)

    def depositar(self, monto):
        self.saldo += monto
        print(f"Depósito de ${monto} realizado. Nuevo saldo: ${self.saldo}")

    def retirar(self, monto):
        print("Operación no permitida. Esta tarjeta no es bancaria.")

# Instanciar tarjetas
tarjetas = []
for i in range(2):
    serie = input(f"Ingrese la serie de la tarjeta {i + 1}: ")
    saldo = float(input(f"Ingrese el saldo inicial de la tarjeta {i + 1}: "))
    
    if i % 2 == 0:
        tarjeta = TarjetaBancaria(serie, saldo)
        if tarjeta.esta_cerca_expiracion():
            print("Tarjeta cerca de expirar.")
    else:
        tarjeta = TarjetaNoBancaria(serie, saldo)

    tarjetas.append(tarjeta)
