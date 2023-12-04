#Programa para ejemplificar el uso de % en formateo de cadenas.

x=15
y=22.45

str1="El numero %d es impar" %x
str2="El numero %f es float" %y

print("Cadena 1 con \% d")
print(str1)
print("Cadena 2 con \% f")
print(str2)

print(type(str1))
print(type(x))
print(f"El numero {x} algo {y}")