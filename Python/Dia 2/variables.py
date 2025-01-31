# las variables son contenedores de datos (str, int, float, etc) que se puden sobreescribir
from time import process_time_ns

nombre="Juan"
print(nombre)
nombre = "Laura"
print(nombre)
edad = 15
edad2 = 30
print(edad + edad2) #Realizar operaciones dentro del print con uso de variables
nombre =input("Dime tu nombre: ")
print("Tu nombre es: " + nombre)
nombre3= "Jose"
nombre4 = "Cara de cola"
frase = nombre3 + nombre4
print(frase)