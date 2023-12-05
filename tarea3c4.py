import math

def calcular_area(tipo_figura, *args):
    if tipo_figura == "triangulo":
        base, altura = args
        return 0.5 * base * altura
    elif tipo_figura == "cuadrado":
        lado = args[0]
        return lado * lado
    elif tipo_figura == "rectangulo":
        base, altura = args
        return base * altura
    elif tipo_figura == "circulo":
        radio = args[0]
        return math.pi * radio * radio
    else:
        return "Figura no válida"

# Ejemplos de uso
print("Área del triángulo:", calcular_area("triangulo", 6, 4))
print("Área del cuadrado:", calcular_area("cuadrado", 5))
print("Área del rectángulo:", calcular_area("rectangulo", 8, 3))
print("Área del círculo:", calcular_area("circulo", 5))