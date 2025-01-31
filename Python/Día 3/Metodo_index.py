# El metodo index () nos puede ayudar de diferentes maneras. Dos de los casos son el buscar el el indice de una letra
# dentro de una serie de cadenas de texto:
from operator import index

mi_texto =  "hola"
print(mi_texto.index("o"))
# Despues podemos saber que letra esta en un determiando inidce:
print(mi_texto[3])
# Los indices en python siempre empiezan del 0. se pueden usar numeros megativos para contar de derecha a izqierda, solo
# que igual que usando nuemros positivos, el 0 estará en la izquiera y el -1 en el extremo derecho.

texto = "Esta es una prueba"
resultado = texto[-1]
print(resultado)
print(texto.index("a"))
#print(texto.index("x")) nos muestra unn error al no encontrar el caracter y rompe el codigo
print(texto.index("prueba")) # Muestra a partir de que indice empieza la palabra
#print(texto.index("prueva")) # Si la palabra está malñ escrita, nos arroja un error, así como el hecho de que es
                             # sensible a las mayusculas
print(texto.index("a",5,11)) # El uso de .index se puede espcificar luego de esceribir el caracter a
                                                # buscar, separado por comas es desde donde inicia la busqueda y donde
                                                # termnina de buscar. Solo que no es inclusivo, es despues del inicio y
                                                # antes del fin de la busqueda.
print(texto.rindex("a")) #Busca de derecha a izquierda




