# Crear un programa que pida al usuario ingresar un texto y que ingrese tres letras a su eleccion 
# Cuantas veces aparecen las letras que eligió 
# Cuantas palabras hay en el texto
# Cual es la primer letra y la ultima 
# Mostrar el texro en modo inverso 
# Ver si aparece la palabra {'Python'} en el texto
print('Bienvenido al analizar de textos, a continuacion le pediremos que ingreses una seria de palabras a tu eleccion, por lo que continua adelante')
print('Tambien te pediremos que ingreses 3 letras aleatorias separadas por un espacio')
texto = input('Ingresa aquí tu texto a elección: ')
letras = input('Ingresa aqui tus letras: ').lower()
lista_letras = letras.split()
lista_texto = texto.split()
texto_inverso = texto[::-1]
texto_min = texto.lower()
print("Hemos encontrado la cantidad de letras " +lista_letras[0]+ " de: {}".format(texto_min.count(lista_letras[0])))
print("Hemos encontrado la cantidad de letras " +lista_letras[1]+ " de: {}".format(texto_min.count(lista_letras[1])))
print("Hemos encontrado la cantidad de letras " +lista_letras[2]+ " de: {}".format(texto_min.count(lista_letras[2])))
print("\n")
print('Tu texto tiene un total de palabras de: {}'.format(len(lista_texto)))
print("\n")
print(f"Tu primer letra es '{texto[0]}' y la ultima es '{texto[-1]}'")
print("\n")
palabra = 'Python' in texto
dic = {True:"Sí", False:"No"}
print('Python se encuentra dentro del texto que escribiste??: {}'.format(dic[palabra]))
print("\n")
lista_texto.reverse()
texto_invertido = ' '.join(lista_texto)
print('A continuación te mostraré el texto a la inversa: ')
print(texto_invertido)

