import math

def fun1(a,b,c):
    d=(b*b)-4*a*c
    def fun2():
        nonlocal d,a
        if d==0:
            x1=(-b+math.sqrt(d))/a
            x2=x1
        else:
            x1=(-b+math.sqrt(d))/2*a
            x2=(-b-math.sqrt(d))/2*a
        s=tuple([float("%.3f"%x1),float("%.3f"%x2)])
        return s
    return fun2()

print(fun1(1,1,-1))

import math

def resolver_ecuacion_cuadratica(a, b, c):
    delta = (b * b) - 4 * a * c

    def calcular_raices():
        nonlocal delta, a

        if delta >= 0:
            # Raíces reales
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
        else:
            # Raíces complejas conjugadas
            parte_real = -b / (2 * a)
            parte_imaginaria = math.sqrt(abs(delta)) / (2 * a)
            x1 = complex(parte_real, parte_imaginaria)
            x2 = complex(parte_real, -parte_imaginaria)

        return x1, x2

    return calcular_raices()

# Ejemplo de uso
raices = resolver_ecuacion_cuadratica(1, 1, -1)
print("Raíces:", raices)


'''
falta implementar solucion a numeros o raices complejas
un numero complejo esta hecho por un positivo y un negativo.
si delta es menor a cero se produce un numero complejo conjugado
-b+sqrtdelta/2a
como castear un numero complejo
'''