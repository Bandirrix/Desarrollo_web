'''
El programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una serie
de guiones que representa la cantidad de letras que tiene la palabra. El jugador en cada turno
deberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a
mostrar en qué lugares se encuentra. Pero si el jugador dice una letra que no se encuentra en
la palabra oculta, pierde una vida.

Primero vas a crear un código que importe el método choice, ya que lo vas a necesitar
para que el sistema pueda elegir una palabra al azar dentro de una lista de palabras que
también vas a crear al comienzo.
 Luego de eso, vas a crear tantas funciones como creas necesarias para que el programa
haga cosas como pedirle al usuario que elija una letra, para corroborar si lo que el usuario
ha ingresado es una letra válida, para chequear si la letra ingresada se encuentra en la
palabra o no, para verificar si ha ganado o no, etc.
 Recuerda escribir primero las funciones y luego el código que las implementa
ordenadamente. 
'''
from random import *

print("Bienvenido al juego del 'Ahorcado'. \nEstás listo para comenzar??")
palabras_secretas = ["carro", "cama","programar", "laptop", "silla"]
palabra_random  = choice(palabras_secretas)
print(palabra_random)
contador_vidas = len(palabra_random)
print(contador_vidas)


def mostrar_palabra ():
    print("La palabra del juego ha sido escogida satisfactoriamente. \nA continuación te apareceran los espacios correspondientes:")
    longitud = len(palabra_random)
    lista = []
    for i in palabra_random:
        lista.append("_")

    print(" ".join(lista))
    return lista
 
def verificacion_letra ():
    letra =  input("Elige una letra: ")
    if letra in palabra_random:
        print("la letra sí está correcta")
        return True
    else: 
        print("está mal")
        return False
        
mostrar_palabra()     
while contador_vidas != 0:
    if verificacion_letra() == True:
        print("Nose")
    else:
        contador_vidas -= 1
        print(contador_vidas)

    #for letra in pala
    # funcion para pedir la letra a analizar 
    # funcion para poder analizar la letra 
# funcion para modificar la lista con los aciertos 
# funcion para quitar vidas del contador 
# funcion para poder mostrar el resultado 



