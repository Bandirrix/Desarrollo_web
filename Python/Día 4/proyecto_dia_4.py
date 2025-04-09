from random import *

print('Bienvenido a adivina el numero mi estimado rey')
nombre = input("Cuál es tu nombre mi extraño viajero?: ")
print(f"Estás listo para jugar {nombre}? Vamos a ello que tienes que adivinar un numero del 1 al 50")
numero_user = int(input("Dime un valor numerico entre el rango que acordamos"))
numero_maquina = randint(1,100)
intentos = 8
print(numero_maquina)
while intentos > 0:
	if numero_user == numero_maquina:
    	print(f'Has ganado {nombre}, numero que pensé era: {numero_maquina}')
    	print(f'tomado Te ha solo: {intentos} intentos ')
	elif numero_user < 1 or numero_maquina > 100:
    	print('Has escogido un número que está fuera del rango :()')
	elif numero_user < numero_maquina:
    	print('Tu numero es más pequeño del que yo elegi, sigue intentando')
	elif numero_user > numero_maquina:
    	print('El numero que elegiste es mayor al que yo tengo, vuelve a intentarlo')
else:
	intentos = intentos -1
	numero_user = int(input('Dime otro numero: '))
        


