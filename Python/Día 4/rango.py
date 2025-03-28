# Rango (range) es una función que permiter crear una cantidad de numeros sin tener que crear una variable o una lista
# Los range solo pueden ser usados con int, no con float

for numero in range(5): #Aqui por defecto empieza en 0, sin tomar el cuenta el numero que pusiste
    print(numero)

for numero in range(1,5): #Aqui el primer numero indica cual esl numero de partida
    print(numero)

for numero in range(1,100,2): #El ultimo numero indica cada cuantos numeros este se ejecutará
    print(numero)

lista = list(range(10)) #Se puede hacer el uso de range para poder crear una serie de numeros sin necesidad de tener que declarar cada numero
print(lista)