import random

diccionario_edades = {}
for i in range(100):
    edad = random.randint(0, 100)
    if edad <= 12:
        diccionario_edades[edad] = "Niño"
    elif 13 <= edad <= 18:
        diccionario_edades[edad] = "Adolescente"
    elif 19 <= edad <= 60:
        diccionario_edades[edad] = "Adulto"
    else:
        diccionario_edades[edad] = "Anciano"

for rango, categoria in diccionario_edades.items():
    print(f"Rango {rango}: {categoria}")

arreglo_ninos_pequenos = [edad for edad in diccionario_edades if 0 < edad < 6]
print("Arreglo de niños pequeños:", arreglo_ninos_pequenos)