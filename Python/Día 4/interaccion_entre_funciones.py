from random import shuffle

# Crear un alista inicial con el contenido de los palitos
palitos = ['-', '--', '---', '----']

# Mezclar los palitos
def mezclar (lista):

    shuffle(lista)
    return lista

# Pedirle el intento del palito que quiere
def probar_suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input('Elige un numero del 1 al 4: ')

    return int(intento)

# Comprobar si ha acertado o no
def comprobar_intento (lista,intento): 

    if lista[intento -1] == '-':
        print('A lavar los trastes que has perdido')
    else:
        print('Te has salvado esta vez, pero no volverá a suceder')

    print(f'Te ha tocado el {lista[intento-1]}')

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
comprobar_intento(palitos_mezclados,seleccion)
