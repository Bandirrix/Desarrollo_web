# Los loops en python son bloques de codigo que nos pueden ayudar para poder reproducir lineas de codigo bajo ciertas condiciones en especifico
# Tú puedes indicar el numero de veces que quieres que se itere el programa, o hasta que cumpla una condición 
# En la programcion hay objetos que son iterables, como las listas ya que pudes hacer una repeticion por cada objeto de la lista 

#EN los bucles For se usa esta palabra reservada para indicar "por cada" en una lista, para hcer cierta accion. En este caso se repetira el numero de veces de la cantidad de elementos de la lista
# for item in nombre: print("Hola")

lista = ['a','b','c']
for hola in lista: #Se declara una variable nueva que es letra
    print("Letra: " + hola)

for letra in lista:
    numero_letra = lista.index(letra) + 1 # Aqui se hace una variable para poder ir recorriendo cada uno de los valores con su indice
    print(f"Letra {numero_letra}: {letra}")

lista_nombres = ['luis','fernando','valeria','lizette']
for nombre in lista_nombres:
    if nombre.startswith('l'): #Propiedad que nos permite obtener el valor del primer caracter
        print(nombre)
    else:
        print("Este nombre no comienza con 'l'")

numeros = [1,2,3,4,5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero # por cada vuelta va sumando y almacenando el valor de la vuelta
    print(mi_valor)                              #Aquí es importante tener en cuenta la identación de las cosas, ya que este print es el mismo que el siguiente, pero al estat dentr del ciclo, va imprimiendo el valor en cada vuelta, siendo que el siguiente solo imprime el valor final
print(f"El valor final de esto es: {mi_valor}") 

for a in "pythoon": #Se puede poner directamente el objeto a iterar dentro del mismo ciclo for
    print(a)

for b in [1,2,3,4,5]:
    print(b)

for c,d in [[1,2],[3,4],[5,6]]: #Se puede hacer una doble iteracion en una vuelta, con el primer variable le el primer valor de la lista y el otro con la siguiente
    print(c)
    print(d)

dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}
for item in dic:
    print(item)

for item in dic.items():
    print(item)

for item in dic.values():
    print(item)