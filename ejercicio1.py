#Tarea:Recibir 6 nombres de materia por teclado y sus calificaciones(int/float).
#imprime lista de tuplas.
#imprime dccionario.
#itera sobre x,y en diccionario para hacer una impresion vertical
#imprimir promedio

# Función para recibir nombres y calificaciones
def recibir_datos():
    materias = []
    calificaciones = []
    
    for i in range(6):
        nombre = input(f'Ingrese el nombre de la materia {i+1}: ')
        calificacion = float(input(f'Ingrese la calificación de {nombre}: '))
        
        materias.append(nombre)
        calificaciones.append(calificacion)
    
    return materias, calificaciones

# Función para imprimir lista de tuplas
def imprimir_tuplas(materias, calificaciones):
    lista_tuplas = list(zip(materias, calificaciones))
    print(lista_tuplas)

# Función para imprimir diccionario
def imprimir_diccionario(materias, calificaciones):
    diccionario = dict(zip(materias, calificaciones))
    print(diccionario)

# Función para imprimir verticalmente el diccionario
def imprimir_vertical(diccionario):
    for materia, calificacion in diccionario.items():
        print(f'{materia}: {calificacion}')

# Función para calcular el promedio
def calcular_promedio(calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)
    return promedio

# Main
if __name__ == "__main__":
    materias, calificaciones = recibir_datos()
    
    # Imprimir lista de tuplas
    imprimir_tuplas(materias, calificaciones)
    
    # Imprimir diccionario
    imprimir_diccionario(materias, calificaciones)
    
    # Imprimir verticalmente el diccionario
    diccionario = dict(zip(materias, calificaciones))
    imprimir_vertical(diccionario)
    
    # Calcular promedio
    promedio = calcular_promedio(calificaciones)
    print(f'El promedio es: {promedio}')
