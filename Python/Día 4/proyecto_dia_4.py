from random import *

print('Bienvenido a adivina el numero mi estimado rey')
nombre = input("Cuál es tu nombre mi extraño viajero?: ")
print(f"Estás listo para jugar {nombre}? \nVamos a ello, que tienes que adivinar un numero del 1 al 100")

numero_maquina = randint(1,100)
intentos = 0
while intentos < 8:
	numero_user = int(input("Dime un valor numerico entre el rango que acordamos: "))
	intentos = intentos +1
	if numero_user == numero_maquina:
		print('Acertaste :D')
		print(f'Lo has logrado en: {intentos} intentos')
		break
	elif numero_user > 100 or numero_user < 1:
		print('No has esogido el valor que habíamos acordado, inicia el programa de nuevo')
		break
	elif numero_user > numero_maquina and numero_user < 101:
		print('Tu numero es mas grande que el mio, escoge otro: ')
	elif numero_user < numero_maquina and numero_user < 101:
		print('Tu numero es mas pequeño que el mio, escoge otro: ')
else: 
	print(f'Lo siento {nombre} :(, no pudiste adivinar el numero')
	print(f'El número que he escogido era el: {numero_maquina}')
		


        


