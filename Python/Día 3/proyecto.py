# Crear un programa que pida al usuario ingresar un texto y que ingrese tres letras a su eleccion 
# Cuantas veces aparecen las letras que eligió 
# Cuantas palabras hay en el texto
# Cual es la primer letra y la ultima 
# Mostrar el texro en modo inverso 
# Ver si aparece la palabra {'Python'} en el texto
print('Bienvenido al analizar de textos, a continuacion le pediremos que ingreses una seria de palabras a tu eleccion, por lo que continua adelante')
print('Tambien te pediremos que ingreses 3 letras aleatorias separadas por un espacio')
texto = input('Ingresa aquí tu texto a elección: ')
letras = input('Ingresa aqui tus letras: ')
lista_letras = letras.split()
lista_texto = texto.split()
texto_inverso = texto[::-1]
texto_min = texto.lower()
print('Tu texto tiene un total de palabras de: {}'.format(len(lista_texto)))
print('Tu primer letra es ' + texto[0] + ' y la ultima es ' + texto[-1])
palabra = 'Python' in texto
print('Python se encuentra dentro del texto que escribiste??: {}'.format(palabra))
print(texto)
print(letras) 
print(texto_inverso)
