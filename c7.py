import matplotlib.pyplot as plt
'''#FIG VENTANA
#AX DIVIDIR DE MANERA EQUITATIVA
#PLOTDEFINICION DE LAS LINEAS QUE SE VEN
fig,ax=plt.subplots()
materias=['POO', 'MVC', 'POE', 'PB']
calificaciones={'Jair':[50,60,50,70], 'Odette':[60,60,80,80]}
ax.plot(materias, calificaciones['Jair'],'*', color=(0.2,0.1,0.33))
ax.plot(materias, calificaciones['Odette'],color='k')
plt.show()
'''
'''
import numpy as np
#import math
x=np.linspace(-100,0.01,100)
y=np.sin(x)
fig,ax=plt.subplots(figsize=(3,3))

ax.plot(x,y)
plt.show()
'''
'''
import numpy as np
#import math
x=np.linspace(0,2*np.pi,128)
y=np.sin(x)
yy=np.cos(x)

fig,ax=plt.subplots(figsize=(3,3))
ax.set_title('Grafica')
ax.plot(x,y, label='sen(x)',color=(0.18,0.25,0.33))
ax.plot(x,yy, label='cos(x)',color='b')

ax.legend()
plt.show()

'''


#Lo primero importamos los  modulos necesarios.
import numpy as np

#Declaramos las funciones
def FuncionParabolica(x):
  return x**2/3+3*x**2
def DerivadaParabolica(x):
  return 20*x/3
#Con este array configuramos rango de valores para x de la parabola.
RangoValores_x=np.linspace(-10,10,200)
#Rango -10 de valor inicial, hasta 10,con 200 elementos en eje x desde -10 hasta 10
#print(RangoValores_x)
#Determinamos el rango de valores de la derivada, a partir de Rango de Valores en x.
# Calculamos los valores en y correspondientes al rango de valores de x.
Valores_y = FuncionParabolica(RangoValores_x)
#Calculamos los valores en y correspondientes a la derivada de valores en x.
ValoresDerivada_y = DerivadaParabolica(RangoValores_x)
#print(Valores_y)
#print("*************************************************")
#print(ValoresDerivada_y)
 
#Ahora establecemos parámetros.
Punto_x_Inicial=8 #Punto inicial a partir del cual calculamos la regresion.
TasaDeAprendizaje=0.01#Tasa de Aprendizaje o learning Rate.
Iteraciones=1000 #Vueltas o interaciones.
#Inicializamos arrays para guardar valores de x,y.
Acumulado_x=[Punto_x_Inicial]
Acumulado_y=[FuncionParabolica(Punto_x_Inicial)]
 
#Abrimos un bucle for para iniciar la derivada descendente.
for _ in range(Iteraciones):
  Punto_x_Inicial=Punto_x_Inicial-TasaDeAprendizaje*DerivadaParabolica(Punto_x_Inicial)
  Acumulado_x.append(Punto_x_Inicial)
  Acumulado_y.append(FuncionParabolica(Punto_x_Inicial))
 
print('\n')
print("**************************************************************")
# Encuentra el valor mínimo de la derivada descendente
valor_minimo_derivada = min(Acumulado_y)
print("Valor mínimo de la derivada descendente:", valor_minimo_derivada)
print("***************************************************************")
print('\n')
 
plt.figure(figsize=(10, 6))
 
 
# Graficamos la parábola y el proceso de gradiente descendente.
plt.figure(figsize=(10, 6))
plt.plot(RangoValores_x, Valores_y, label='f(x)=x**2/3+3x**2')
plt.scatter(Acumulado_x, Acumulado_y, color='red', label='Descenso de Gradiente')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Función y Descenso de Gradiente')
plt.grid(True)
plt.legend()
 
plt.show()