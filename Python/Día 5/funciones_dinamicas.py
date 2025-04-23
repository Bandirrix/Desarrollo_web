# Dentro del mundo de las funciones se puede incorporar diversas syintaxis de codigo para poder hacer más completo nuestro código 

def verificacion_3_cifras (numero):
    return numero in range(100,1000) # Devuelve un valor booleano ya que solo checa si el valor a verificar está comprendido dentro de este rango
    # suma = 10+990 : También se podría que ejecute la comparativa usando el resultado de una operación si tener tal cual el valor

resultado = verificacion_3_cifras(600)
print(resultado)

def checar_3_numeros (lista):
    '''
    En este tipo de función hace una verificación con el bucle for para poder encontrar un valor en el rango. Si este ecuentra un numero con las caracteristicas
    adecuadas, return es un objeto que rompe el ciclo del codigo, por lo que no continuará verficando los demás numeros.
    '''
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass

resul = checar_3_numeros([10,60,2000])
print(resul) #Esta función devuelve un valor del tipo 'None' ya que al no cumplirse ninguna condición, este tiene que sí o sí regresar un valor, por lo que regresa este tipo de valor

resul = checar_3_numeros([10,60,200])
print(resul)

def consulta_3_numeros (lista):
    '''
    Este codigo sí devuelve un false cuando no encuntra el valor en el rango permitido
    No funciona si se pone el 'return' false dentro del else, ya que al no cumplir con la condición del rango, automaticamente entra a hacer la verificación del else y como sí cumple, da como resultado False sin necesiad de verificar los demás numeros de la lista
    Cuando no encontró que ningún valor con las condiciones establecidas, rompe el ciclo y regresa el False
    '''
    lista_3_digitos = []
    for n in lista:
        if n in range(100,1000):
            lista_3_digitos.append(n)
        else:
            pass
    
    return lista_3_digitos

resul = consulta_3_numeros([10,600,200,998])
print(resul)