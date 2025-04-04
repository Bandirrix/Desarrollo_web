from random import *

print('Bienvenido a adivina el numero mi estimado rey')
nombre = input("Cuál es tu nombre mi extraño viajero?: ")
print(f"Estás listo para jugar {nombre}? Vamos a ello que tienes que adivinar un numero del 1 al 50")
numero_user = input("Dime un valor numerico entre el rango que acordamos")
numero_maquina = randint(1,50)
intentos = 8
print(numero_maquina)
while numero_user != numero_maquina or intentos == 0:
    numero_user = input("Dime un valor numerico entre el rango que acordamos")
    intentos = intentos -1

