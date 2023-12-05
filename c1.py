'''
a=7     #int
b='a'   #str
c=13.5  # float
d='Hol' #str

print(d+b)
print(d+b*3)

print(type(d+b)) #Informacion del tipo de dato

'''

'''
#PROGRAMA PARA EJEMPLIFICAR EL USO EN FORMATEO DE CADENAS
x=15
y=22.45
str1="el numero %d es impar" %x  #IMPRESION DE TIPO INT
str2= "el numero %f es float" %y #IMPRESION DE UN TIPO FLOAT

print("Cadena 1 con \% d") 
print(str1)                 #IMPRESION DE CADENA COMPLETA
print("cadena 2 con \% f")  
print(str2)                 #IMPRESIONN DE CADENA COMLETA

print(type(str1))  #TIPO DE DATO PARA STR
print(type(x))     #TIPO DE DATO PARA X

#UN EJEMPLO USANDO FORMAT():

str3="El numero {} es un int y el numero {} es un float".format(x.y)
print(str3)


st1='holamundo'
print(st1.capitalize())
print(st1.upper())
print(st1.isalpha())

st2='12345'
print(st2.isalnum())

'''

a=(input('Dame un numero: ')) #ingresa cadena por teclado
b=(input('Dame otro numero: ')) #ingresa cadena por teclado
print(a+b) #CONCATENA LOS VLORESs
a=int(input('Dame un numero: '))
b=float(input('Dame otro numero: '))
print(a+b)
