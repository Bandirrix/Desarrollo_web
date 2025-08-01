def doble_cero (*args):
    contador = 0 #Con esta linea se genera un contador con el cual se hará uso de los indices de la lista 
    for i in args:
        if contador +1 == len(args): #Esta linea es un tope para evitar problemas al tener un cero al final del codigo, ya que trata de verificar el siguiente numero al 
            return False             # cumplir con la siguiente condición, no encuntra el numero y rompe el codigo, por eso si el contador cumple con la longitud, por defecto arroja False
        elif args[contador] == 0 and args[contador + 1 ] == 0: #Doble verificacion donde si se tiene un 0, aumenta un indice y verifica si el siguiente es 0
            return True
        else:
            contador += 1

    return False

print(doble_cero(1,2,3,5,6,7,8,0,0))