
import matplotlib.pyplot as plt
fig,ax=plt.subplots()
materias=['poo','mvc','poe','pb']
calificaciones={'jair':[50,50,50,45], 'odette':[70,75,80,60]}
ax.plot(materias,calificaciones['jair'],'-*',color='blue')
ax.plot(materias,calificaciones['odette'],color='pink')
plt.show()
"""
"""
import matplotlib.pyplot as plt
import numpy as np
import math
x=np.linspace(0,2*np.pi,128)
y=np.sin(x)
yy=np.cos(x)

fig,ax=plt.subplots(figsize=(5,3))
ax.set_title('armonicas')
ax.plot(x,y, label='sen(x)',color='r')
ax.plot(x,yy, label='cos(x)')
ax.legend()

plt.show()



"""
import math
def fun1(a,b,c):
	x=(b*b)-(4*a*c)

	def fun2():
		nonlocal x,a
		if x==0:
			print("valor igual a 0")
		else:
			x1=(-b+math.sqrt(x))/2*a
			x2=(-b-math.sqrt(x))/2*a
			s=tuple([float("%.3f"%x1),float("%.3f"%x2)])

		return s

	return fun2()

print(fun1(2,2,5))
"""