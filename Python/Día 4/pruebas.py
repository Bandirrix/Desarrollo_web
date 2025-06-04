from random import randint
def lanzar_dados ():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    
    return dado1,dado2
    
def evaluar_jugada (valor1,valor2):
    numero_1 = valor1
    numero_2 = valor2
    suma = numero_1 + numero_2
    if suma <= 6:
        print(f'"La suma de tus dados es {suma}. Lamentable"')
    elif suma > 6 and suma < 10:
        print(f"La suma de tus dados es {suma}. Tienes buenas chances")
    elif suma > 10:
        print(f"La suma de tus dados es {suma}. Parece una jugada ganadora")
        
valor1,valor2 = lanzar_dados()
evaluar_jugada(valor1,valor2)