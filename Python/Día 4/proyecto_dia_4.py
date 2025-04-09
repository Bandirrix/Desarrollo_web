from random import *

print('Bienvenido a adivina el numero mi estimado rey')
nombre = input("Cuál es tu nombre mi extraño viajero?: ")
print(f"Estás listo para jugar {nombre}? Vamos a ello que tienes que adivinar un numero del 1 al 100")
numero_user = int(input("Dime un valor numerico entre el rango que acordamos: "))
numero_maquina = randint(1,100)
intentos = 8
print(numero_maquina)
while intentos > 0:
	if numero_user == numero_maquina:
		print('Acertaste')
	elif numero_user > 100 and numero_user < 1:
		print('No has esogido el valor que habíamos acordado, inicia el programa de nuevo')
		break
	elif numero_user > numero_maquina:
		print('Tu numero es mas grande que el mio, escoge otro: ')
	elif numero_user < numero_maquina:
		print('Tu numero es mas pequeño que el mio, escoge otro: ')
intentos = intentos =- 1
numero_user = int(input(':'))

        


