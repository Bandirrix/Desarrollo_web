# Los elmentos del tipo set son relativamentes parecidos a lo de los diccionarios, solo que en este caso se declaran de difente manera 
# Son inmutables y estos no pueden tener valores duplicados porque python los descarta
# No estan ordenados en indice, si bien si tienen un orden especifico
# Se pueden declarar de dos maneras, usando la palabra 'set' usando algun tipo de corchete o si bien, solo poniendo directamente dentro de un conjunto de llaves '{}'
# Los sets solo aceptan un solo argumento con diferentes tipos de valores
# No admite listas ni diccionarios, pero si tuples

mi_set = set([1,2,3,4,5]) #Manera de declarar un set
# mi_set = set(1,2,3,4,5) Esto lo detecta como varios argumentos por que no tiene el juego de parentesis que necesita los set 
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3,4,} #Otra manera de poder declarar un SET
print(type(otro_set))
print(otro_set)
 # 
mi_set2 = set((1,1,1,1,12,2,(2,5,4),6)) #No se puede repetir valores, pero si admite tuples
print(mi_set2)
print(len(mi_set))
print(2 in mi_set) # Buscar un elemento dentro de un SET

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2) #Metodo union para convinar sets (esto elimina valores repetidos)
print(s3)
s1.add(4) #Add agrega un valor al set
s1.remove(3) #Remove elimina elementos del set
s1.discard(6) #Discard percido a remove, pero no marca error cuando no hay elementos
sorteo = s1.pop() #Elimina un valor aleatorio ya que no hay un orden dentro de esto
s1.clear() #Elimina todo lo del set si no especifica ningun valor
print(sorteo)
print(s1)
