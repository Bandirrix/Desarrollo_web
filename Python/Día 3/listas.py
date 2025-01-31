# Las listas son un conjuto de datos organizados dentro de una variable 
# Estas estan dentro de corchetes [] y estan separados por una ","
# Las listas pueden contener strings, int, float. Y puede contener llistas dentro de las listas
# A su vez, estas pueden cambiar el orden, sacar valores e imprimirlos

mi_lista = ['a','b','c']
mi_lista_2 = ['hola',55,65.2]
print(type(mi_lista))
print(len(mi_lista)) # Imprimir longitud de las listas 
resultado = mi_lista[0] #impimir un valor especifico segun su indice
print(resultado)
resultado = mi_lista[0:2] #Imprpimir los datos de la lista segun sus indices
print(resultado)
print(mi_lista + mi_lista_2) #Concatenar listas
mi_lista3 = mi_lista + mi_lista_2
print(mi_lista3)

mi_lista3[0] = 'alfa' #Sobrescribir valores de las listas
print(mi_lista3[0])
mi_lista3.append('g') # Agregar un elementos
print(mi_lista3)
mi_lista3.pop() #Metodo para eliminar valor de lista. Si no se especifica el indice, se elimina el ultimo valor
mi_lista3.pop(0)
eliminado = mi_lista3.pop(0) #agregar elemento eliminado en una variable
print(mi_lista3)
print(eliminado)

lista = ['g','o','m','c','a']
lista.sort() #ordena alfabeticamente
# Nota: Tanto sort como reverse
print(lista)
lista.reverse() #Ordena los valores de manera inversa, de mayor a menor
print(lista)