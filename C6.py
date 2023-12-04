"""def fun1(c): #c es  local (esta en ambas funciones)
	c=c*2
	def fun2(c):
		print('Texto: ',c)

	fun2(c)

fun1('Hola mundo')
"""


"""def fun1():
	n=1
	def fun2():
		nonlocal n
		r=n+1
		return r 

	return func2()

print(fun1())"""

import math

def fun1(a,b,c):
	d=(b*b)-4*a*c
	def fun2():
		nonlocal d,a
		if d==0:
			x1=(-b+math.sqrt(d))/2*a
			x2=x1
			s=tuple({float("%.3f"%x1),float("%.3f"%x2)})
		else:
			x1=(-b+math.sqrt(d))/2*a
			x2=(-b-math.sqrt(d))/2*a
			s=tuple({float("%.3f"%x1),float("%.3f"%x2)})

		return s
	return fun2()


print(fun1(1,1,-1))


	