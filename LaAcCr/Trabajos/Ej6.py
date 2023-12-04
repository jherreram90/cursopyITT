#------------------funciones envolventes------------

"""
def fun1(c):#c es local porque etsa en ambas funciones 
	#c=c*2
	def fun2(c):
		print('text: ', c)

	fun2(c)


fun1('Hola mundo')
"""
"""
def fun1():
	n=100
	def fun2():
		#nonlocal n
		r=n+1
		return r
	return fun2()

print(fun1())
"""

import math
def fun1(a,b,c):
	x=(b*b)-(4*a*c)

	def fun2():
		nonlocal x,a
		if x==0:
			#print("valor igual a 0")
			x1=(-b+math.sqrt(x))/2*a
			x2=x1
			s=tuple([float("%.3f"%x1),float("%.3f"%x2)])

		elif x<0:
			x1a=(-b)/2*a
			x1b=(math.sqrt(-1*x))/2*a
			x1=str("%.3f"%x1a)+'+'+str("%.3f"%x1b)+'i'

			x2a=(-b)/2*a
			x2b=(math.sqrt(-1*x))/2*a
			x2=str("%.3f"%x2a)+'+'+str("%.3f"%x1b)+'i'

			s=tuple([x1,x2])

		else:
			x1=(-b+math.sqrt(x))/2*a
			x2=(-b-math.sqrt(x))/2*a
			s=tuple([float("%.3f"%x1),float("%.3f"%x2)])

		return s

	return fun2()

print(fun1(2,2,5))

