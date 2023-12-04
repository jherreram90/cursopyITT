import numpy as np
import random
import matplotlib.pyplot as plt
from celluloid import Camera


#DEFINICION DE VARIABLES
n=500 #CANTIDAD DE CELULAS
t=250 #TIEMPOS DISCRETOS

#DEFINICION DE LIMITAS PARA EL GRAFICO
xmi=-20
xma=20
ymi=-20
yma=20

'''
Lo siguiente genera de forma aleatoria el estado unicias (posicion)
de cada una de las celulas
'''
x=np.random.randint(5,size=n) #coordenada aleatoria
y=np.random.randint(5,size=n) #coordenada aleatoria

f=np.zeros(n)

#Lo siguiente define algunas cosas para la grafica

fig=plt.figure() #ventana vacia para graficar
camara=Camera(fig)
plt.xticks(range(xmi, xma, 1)) #Modifica la escala del x
plt.yticks(range(ymi, yma, 1)) #Modifica la escala del y
plt.grid(True) #Dibuja una cuadricula
plt.axis([xmi, xma, ymi, yma]) #Esto modifica limites del grafico
plt.title('AC-Movimiento aleatorio')

 #CONTINUACION SE MODELA Y SIMULA EL MOVIMIENTO ALEATORIO DE CADA UNA DE LAS CELULAS T-TIEMPOS DISCRETOS

for i in range(t): #Este buvle es para tiempos discretos
    for j in range(len(x)): #Este bucle recorre celuas
        plt.plot (x[j], y[j], 'o', color=[0.2,0.5,0.7])
        f[j]=random.random() #genera numero aleatorio y lo guarda
        if 0<f[j]<0.20:
            x[j]=x[j]+1
        elif 0.20<f[j]<0.40:
            x[j]=x[j]-1
        elif 0.40<f[j]<0.60:
            y[j]=y[j]+1
        elif 0.60<f[j]<0.80:
            y[j]=y[j]-1
        else:
            x[j]=x[j]
            y[j]=y[j]
    camara.snap()
    
animation=camara.animate(interval=100, repeat=False)
plt.show()

#COMO QUITAR LOS NUMEROS DE IZQUIERDA SIN AFECTAR EL 'GRID', BOTONES