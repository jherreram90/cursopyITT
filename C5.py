"""def fun1(c):#c es local(esta en ambas funciones)
	c=c*2
	def fun2(c):
		print('Texto: ', c)

	fun2(c)

fun1('Hola mundo')"""

#decorador, funciones que envuelven otras funciones para modificar sus comportamientos...
"""def fun1():
	n=100
	def fun2():
		nonlocal n
		r=n+1
		return r

	return fun2()

print(fun1())"""

from math import sqrt

def fun1(a,b,c):
    n= b * b - 4 * a * c
    def fun2():
        if n<= 0:
            raiz = sqrt(n)
            x1 = (-b + raiz) / (2*a)
            x2 = (-b - raiz) / (2*a)
            d = tuple([x1, x2])
            #d=tuple([float("%.3f"%x1), float("$.3f"%x2)])
            return d
        else:
            return None

    return fun2()

print(fun1(1,2,1))


#delta tal cual raices complejas  x1 y x2 conjunto de numero complejos, parte real y parte imaginaria, con cadena, castear con numero complejos



