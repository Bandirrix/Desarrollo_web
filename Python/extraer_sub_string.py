# slicing se le llama como separar una cadena de caracteres de una cadena mucho mas grande
# Esto se hace con el uso de indices de la siguiente:

texto = "ABCDEFGHIJKMLN"
#fragmento = texto[2]
fragmento = texto[2:5] #En este caso particular, lo que hace es que selecciona todo desde la posicion 2 hasta antes de la 5
print(fragmento)
fragmento = texto[:5] #En este caso, lo que hace es que selecciona todo desde rl inicio hasta antes de la 5
print(fragmento)
fragmento = texto[0:10:2] #Con el tercer parametro indica cadca cuanto se estaria selecionando una letra, en este caso es 1 si y una no
print(fragmento)
fragmento = texto[::2] # Si dejas los parametros vacios, este lo toma desde inicio al fin de la cadena
print(fragmento)
fragmento = texto[::-1] #Con un indice a la -1, imprime las letras de derecha a izquierda
print(fragmento)