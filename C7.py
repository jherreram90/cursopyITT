import matplotlib.pyplot as plt
import numpy as np
import math
"""
fig,ax = plt.subplots() #fig es la ventana # ax dividir el cuadro
materias=['pop', 'mvc', 'poe', 'pb']
calificaciones = {'jair':[45, 65, 80, 100],'odette':[50, 70, 85, 95]}
ax.plot(materias, calificaciones['jair'],'-*',color='blue') # plot 
# valores rgb en decimamles (0.50,0.75, 0.25)
# -o o * son para graficar de manera diferente
ax.plot(materias, calificaciones['odette'],color='k') # color negro
plt.show() # muestra la grafica 
"""


x = np.linspace(0,2*np.pi,128)
y = np.sin(x)
yy = np.cos(x)

fig,ax = plt.subplots(figsize=(10,5))

ax.set_title('grafica')
ax.plot(x,y , label='sen(x)', color = (0.15,0.25,0.35))
ax.plot(x,yy, label='cos(x)', color = (0.75,0.65,0.55))
ax.legend()

plt.show()


"""

def fun1(a,b,c):
	d=(b*b)-4*a*cs
	def fun2():
		nonlocal d,a,b,c
		if d==0:
			x1=(-b+math.sqrt(d))/2*a
			x2=x1
			s=tuple({float("%.3f"%x1),float("%.3f"%x2)})
		elif a==0  b==0:
			d==c
		else:
			x1=(-b+math.sqrt(d))/2*a
			x2=(-b-math.sqrt(d))/2*a
			s=tuple({float("%.3f"%x1),float("%.3f"%x2)})

		return s
	return fun2()


print(fun1(0,0,-1))




