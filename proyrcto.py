''' NOTAS
1 pt
Todo punto calculado debe de mostrarse en el metodo graficar YES
    -------
1 pt
hacer un video explicando el codigo y mostrando la ejecucion (15 min 20 max) 50 50
    -------
1 pt
reporte escrito - 50 50
    -------
1 pt
El polinomio instancia coeficiente de forma aleatoria- YES
    -------
-3 pt
# Si no hay video, reporte, se testea el 15 o no se instancia de forma aleatoria -3pt
    -------
'''

#Importamos la libreria SympY para usar variables simbolicas (x, y)
import pprint
import random
import sympy
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols,Eq,solve,discriminant,simplify,diff
from matplotlib import pyplot
#''' CONTRUCTOR '''
''' RAICES DISCRIMINANTE'''
'''
Discrimitante
-b(-+)/b**2 -4ac
        2a
'''

class Polinomio:
    def __init__(self, grado):
        self.grado = grado
        self.coeficientes = [random.randint(1, 99) * random.choice([-1, 1]) for _ in range(grado + 1)]

    def __str__(self):
        # Construir una cadena que representa el polinomio
        cadena_polinomio = ""
        for i, coeficiente in enumerate(self.coeficientes):
            grado_actual = self.grado - i
            if coeficiente != 0:
                signo = "+" if coeficiente > 0 else "-"
                cadena_polinomio += f" {signo} {abs(coeficiente)}*x^{grado_actual}"

        return cadena_polinomio.lstrip(" +")

    def discriminante(self):
        x = sp.symbols('x')
        polinomio = sp.Poly(self.coeficientes , x)
        discriminante_polinomio = sp.discriminant(polinomio)
        return discriminante_polinomio

    def puntos_extremos(self):
        x = sp.symbols('x')
        polinomio = sp.Poly(self.coeficientes, x)
        derivada = polinomio.diff(x)
        puntos_extremos = solve(derivada, x)
        return puntos_extremos

    def graficar(self):
        x = sp.symbols('x')
        funcion = sp.Poly(self.coeficientes, x)
        x_valores = np.linspace(-50, 50, 400)
        y_valores = np.array([funcion.subs(x, valor) for valor in x_valores])

        plt.figure(figsize=(16, 12))
        plt.plot(x_valores, y_valores, label=str(self))
        plt.axhline(0, color="black")
        plt.axvline(0, color="black")
        plt.xlim(-100, 100)
        plt.ylim(-100, 100)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Gráfica de ' + str(self))
        plt.grid(True)
        plt.show()


# Ejemplo de uso
grado_polinomio = int(input("Grado del polinomio: "))
polinomio = Polinomio(grado_polinomio)

print("Tu polinomio es:", polinomio)
print("El discriminante es:", polinomio.discriminante())
print("Los puntos extremos son:", polinomio.puntos_extremos())
polinomio.graficar()


def discriminante(p1):
#pa wachar https://es.planetcalc.com/8188/
#Recibe los valores p1 lo almacena para usarlo
    polinomio1=p1
#Calcula el discriminante del polinomio usando discriminant que esta pre establecido dentro de la libreria sympy
    discriminante1=discriminant(polinomio1,x)
#Imprime el valor del discriminante
    print("-----DISCRIMINANTES-----")
    print(f"El discriminante del primer polinomio es: {discriminante1}")
''' /RAICES DISCRIMINANTE'''

''' RAICES PUNTOS'''
def puntos(p1):
#Define el polinomio cúbico
    polinomio=p1
#Calcula la derivada del polinomio
    derivada=diff(polinomio,x)
#Encuentra los puntos donde la pendiente es igual a cero
    puntos_extremos=solve(derivada,x)
#Imprime los puntos de la recta recta (extremos del lado recto)
    print("-----PUNTOS-----")
    print("Los puntos de la recta recta (extremos del lado recto) son:")
    for punto in puntos_extremos:
        print(f"x ={punto}")
''' / RAICES PUNTOS'''

''' RAICES FOTO Y DIRECTRIZ'''
#solo aplicable a polinomios de 2 grado pabajo no funciona con polinomios de grado 3 
def fotodirecta(p1):
#Define el polinomio cuadrático de la parábola
    polinomio=p1
#Encuentra la forma canónica de la ecuación de la parábola
    forma_canonica=simplify(polinomio)
#Extrae los coeficientes de la forma canónica
    a,h,k=forma_canonica.as_ordered_terms()
# Calcula el foco y la directriz
    foco_x=h
    foco_y=k+1/(4*a)
    directriz_y=k-1/(4*a)

    # Imprime los resultados
    print("-----foto y disectris-----")
    print(f"La forma canónica de la parábola es: {forma_canonica}")
    print(f"El foco de la parábola es: ({foco_x}, {foco_y})")
    print(f"La ecuación de la directriz es: y = {directriz_y}")

''' GRAFICA'''
# Función cuadrática.
def f1(x,p1):
    return p1
#-Graficar polinomio(Matplotlib)
def grafico(p1):
#pa wachar graficas https://www.geogebra.org/graphing?lang=es
    print("-----GRAFICA-----")
    print("Wachas la grafica de: ")
    # Parsear la función cuadrática ingresada por el usuario.
    funcion=sp.sympify(p1) 
    # Crear un rango de valores de 'x'.
    x_valores=np.linspace(-50, 50,400)
    # Evaluar la función en los valores de 'x'.
    y_valores=np.array([funcion.subs(x,valor) for valor in x_valores])
    # Crear la gráfica.
    plt.figure(figsize=(16,12))#tamaño
    plt.plot(x_valores,y_valores,label=' '+p1) #texto
    plt.axhline(0,color="black")#lineas divisoras
    plt.axvline(0,color="black")#lineas divisoras
    plt.xlim(-100,100)#tamaño a ver
    plt.ylim(-100,100)#tamaño a ver
    plt.xlabel('x')#pues x
    plt.ylabel('y')#pues y
    plt.title('Gráfica de '+p1)#pues titulo
    plt.grid(True)#habilita los cuadritos
    plt.show()
    print("Cerraste la grafica")
    inicios()
''' /GRAFICA'''

''' MAXIMOS Y MINIMOS'''
#>>M(x,y) - m(x,y)
''' /MAXIMOS Y MINIMOS'''


##INICIO    
#Definimos los simbolos de sympy a usar en forma global pa usar
sympy.init_printing()
x,y=sympy.symbols('x,y')
    
def inicios():
    print("\n")
    print("-----INICIO-----")
    grado=input("Grado del polinomio: ")
    rambo(int(grado))
    
def rambo(grado):
    gradooriginal=grado #guarda el grado
    valorx="x**"#valor inicial pa duplicar y hacer la magia
    polinomiorambo=""#donde se guardara todo el polinomio nuevo
    for a in range(0,grado): #forcito pa crear la magia
        negaplus=random.choice('-+')#pa agregar un + o -
        n=str(random.randint(1,99))#pa agregar numeros aleatorios
        potencia=str(grado)#pa tranformar el grado recibido de int a str
        polinomiorambo=polinomiorambo+negaplus+n+"*"+valorx+potencia #la concatenacion magica
        grado=grado-1#resta un grado para la nueva concatenacion
    polinomiorambo=polinomiorambo+(str(random.choice('-+')+(str(random.randint(1,99)))))#concatena un numero al final pa que tenga un valor sin x
    print(" Tu polinomio es: ",polinomiorambo)#imprecion
    if(gradooriginal==0):
        print("ingrese un grado valido")
    elif(gradooriginal==2):
        fotodirecta(polinomiorambo)
        puntos(polinomiorambo)
        discriminante(polinomiorambo)#llamada de las cosas
        grafico(polinomiorambo)
    else:
        print("GRADO:",gradooriginal," No tiene Raices")
        grafico(polinomiorambo)
    
    
inicios()

