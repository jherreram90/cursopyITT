import math

def calcular_figura(tipo_figura):
    if tipo_figura == "cuadrado":
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = lado**2
        perimetro = 4 * lado
    elif tipo_figura == "circulo":
        radio = float(input("Ingrese el radio del círculo: "))
        area = math.pi * radio**2
        perimetro = 2 * math.pi * radio
    elif tipo_figura == "triangulo":
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = (base * altura) / 2
        perimetro = None
    elif tipo_figura == "pentagono":
        lado = float(input("Ingrese el lado del pentágono: "))
        apotema = lado / (2 * math.tan(math.pi / 5))
        perimetro = 5 * lado
        area = (perimetro * apotema) / 2
    elif tipo_figura == "hexagono":
        lado = float(input("Ingrese el lado del hexágono: "))
        apotema = lado / (2 * math.tan(math.pi / 6))
        perimetro = 6 * lado
        area = (perimetro * apotema) / 2
    else:
        print("Tipo de figura no válido.")
        return None, None

    return area, perimetro

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción que desea (o 'salir' para salir): ")

        if opcion == "salir":
            print("¡Hasta luego!")
            break

        area, perimetro = calcular_figura(opcion)

        if area is not None and perimetro is not None:
            print(f"Área: {area}")
            print(f"Perímetro: {perimetro}")
        elif area is not None:
            print(f"Área: {area}")
        else:
            continue

if __name__ == "__main__":
    main()
