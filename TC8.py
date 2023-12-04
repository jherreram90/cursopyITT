class tajeta(object):
	#docstring for tajeta
	def __init__(self, serie, retiro, deposito, saldo): # definicion del objeto y self es el apuntador al mismo objeto
		# ATRIBUTOS
		self.seri = serie  
		self.reti = retiro
		self.depo = deposito
		self.sald = saldo
#METODOS
	def serie(self):
		num_s = self.seri
		print('Tu numero de serie es: ', num_s)

	def saldo(self):
		saldo_act = self.sald 

		print('Tu saldo actual es: ', saldo_act)

	def fecha_v(self):

		try:
			fecha_u = datetime.strptime(dat_b, "%Y-%m-%d")
		except ValueError:
			print("formaato incorrecto ingresa (AÑO-MES-DIA)")
			return

		# FECHA DEL SISTEMA

		fecha_s = datetime (2040,12,31)
		# DIF FECHAS 

		dif_f = fecha_s - fecha_u
		dif_f1 = int(dif_f.days/365)

		# print ('TU TARJETA VENCE EN: ', int(dif_f.days/365), 'AÑOS')

		if dif_f1 >= 5:
			# SI AUN NO VENCE LA TARJETA
			print ('A TU TARJETA LE FALTAN: ', int(dif_f.days/365), 'AÑOS PARA VENCER')
			# SI YA ESTA A PUNTO DE VENCER
		elif dif_f1 <= 3:
			print ('TU TARJETA VENCE EN: ', int(dif_f.days/365), 'AÑOS')

	def deposito(self):
		saldo = self.depo+self.sald
		print('Deposito de: ', self.depo)
		print('Saldo: ', saldo)
		

	def retira(self):
		saldo = self.sald-self.reti
		print('Retiro de: ', self.reti)



for instanciacion in range(1, 5):
	# INGRESAR LOS DATOS DE LAS TARJETAS 

	num_s = input(str("Ingresa el numero de serie de tu tarjeta: \n"))
	bancari = len(num_s)

	if bancari >= 16: # VALIDACION TARJETA BANCARIO
		print ("TARJETA BANCARIA")
		nip_b = input("NIP: \n")
		cvv_b = input("CVV: \n")
		dat_b = input("FECHA VENCIMIENTO AÑO/MM/DD: \n")
		t1 = tajeta(num_s, 500, 150, 2000)
		t1.fecha_v()
		t1.serie()
		t1.retira()
		t1.deposito()
		t1.saldo()
	elif bancari <= 16: # VALIDACION TARJETA NO BANCARIO
		print ("TARJETA NO BANCARIA")
		t2 = tajeta(num_s, 700, 50, 2000)
		t2.serie()
		t2.retira()
		t2.deposito()