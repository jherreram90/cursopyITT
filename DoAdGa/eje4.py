import random as rd

edades = []

# Función para generar edades aleatorias
def generar_edades():
    for i in range(35):
        edades.append(rd.randint(1, 100))
    return edades

# Función para clasificar las edades
def clasificar_edades(edades):
    niños = []
    jovenes = []
    adultos = []

    for i in edades:
        if i < 6:
            niños.append(i)
        elif 6 <= i <= 45:
            jovenes.append(i)
        elif 46 <= i <= 100:
            adultos.append(i)

    return niños, jovenes, adultos

# Generar edades
generar_edades()

# Clasificar edades
niños, jovenes, adultos = clasificar_edades(edades)

# Mostrar resultados
print("Edades de niños:", niños)
print("Edades de jóvenes:", jovenes)
print("Edades de adultos:", adultos)
