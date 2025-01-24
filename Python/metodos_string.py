# Upper se usa para poder pasar a las mayusculas de una cadena
# Lower para pasar a minusculas
# split separarlo en partes (listas)
# join Unir items usando separadores
# find encontrar un sub-string
# replace reemplazar un substring
# El uso de metodos se suele poner en la variable que se desea trbajar luego de un ".", seguido del metodo que puede llevar mas parametros

texto = "Este es el texto del buen Ferchis"
resultado = texto.upper() #Convierte todas las letras en mayusculas
print(resultado)
resultado = texto[2].upper() #Convierte la seleccion del indice en mayuscula
print(resultado)
resultado = texto.lower() #Convierte la seleccion del indice en minusculas
print(resultado)
resultado = texto.split() #Separa las palabras de una variable en elementos de lista. En este caso, se deja vacio el parentesis y automaticamente usa el espacio como separador
print(resultado)
resultado = texto.split("t") #Separa las palabras de una variable en elementos de lista. En este caso, el parentsis usa el caracter como separador
print(resultado) 

a="Aprender"
b="Python"
c="es"
d="genial"
e = " ".join([a,b,c,d]) #Se establace un espacio en blanco donde se colocara la oracion, haciendo uso de una lista de donde saca los valores. Lo que esta en el parentesis indica el conector que se usara para las palabras
print(e)

resultado = texto.find("t") #Busca e indica en que posicion del caracter
print(resultado)
resultado = texto.find("Ferchis") #Busca e indica en que posicion esta la palabra (donde inicia)
print(resultado)
resultado = texto.find("z") #Si no esta una palabra dentro de la cadena, arroja un 0 y no un error como en el metodo index
print(resultado)

resultado = texto.replace("e","x") #Lado izquierdo indica que se quiere remplazar y lado derecho por cual se va a remplazar
print(resultado) #Nota: Este metodo tiene reglas, como que se hace el cambio literal, es decir, si pones 'e' solo remplaza las 'e' minisculas