"""a= int(input('ingresa a: '))
b= int(input('Ingresa b: '))

def suma(a,b):
	c=a+b
	return c

#print(suma(a,b))
c= suma(a,b)
print (c)
"""

"""import random

# Primera función para generar un diccionario
def generar_diccionario(edades):
    diccionario_edades = {}
    for edad in edades:
        if edad <= 12:
            diccionario_edades[edad] = "Niño"
        elif 13 <= edad <= 18:
            diccionario_edades[edad] = "Adolescente"
        elif 19 <= edad <= 60:
            diccionario_edades[edad] = "Adulto"
        else:
            diccionario_edades[edad] = "Anciano"
    return diccionario_edades

# Segunda función que convierte una lista de edades aleatorias en un diccionario
def convertir_a_diccionario(edades):
    return {edad: "Niño" if edad <= 12 else "Adolescente" if 13 <= edad <= 18 else "Adulto" if 19 <= edad <= 60 else "Anciano" for edad in edades}

# Tercera función que genera un diccionario de niños chiquitos
def generar_diccionario_ninos_chiquitos(edades):
    return {edad: "Niño" for edad in edades if 0 < edad < 6}

# Ejemplo de uso
edades_aleatorias = [random.randint(0, 50) for _ in range(50)]

# Usar la primera función para generar un diccionario
diccionario_generado = generar_diccionario(edades_aleatorias)
print("Diccionario generado por la primera función:")
print(diccionario_generado)

# Usar la segunda función para convertir una lista de edades aleatorias en un diccionario
diccionario_convertido = convertir_a_diccionario(edades_aleatorias)
print("Diccionario generado por la segunda función:")
print(diccionario_convertido)

# Usar la tercera función para generar un diccionario de niños chiquitos
diccionario_ninos_chiquitos = generar_diccionario_ninos_chiquitos(edades_aleatorias)
print("Diccionario de niños chiquitos:")
print(diccionario_ninos_chiquitos)
"""























