# Tipos de listas inmutables que una vez realizados, no pueden modificarse ni alterarse
# Son parecidas a las listas, pero en lugar de hacerlo entre [] se suelen usar parentesis o escribirse sin estos
# Utilizan menos memoria y se procesan mas rapido que las listas (Almecenar estructuras que no queremos que sean eliminadas)
# Incluyen cuaquier tipo de dato
# Se puede indexar y anexar

mi_tuple = (1,2,3,4,(10,20),12)
print(type(mi_tuple))
mi_tuple2 = 1,2,3,4,'hola',3.5
print(mi_tuple2[0])
# mi_tuple[0] = 2 >>>>> Aqui nos deberia de marcar error ya que estos no se pueden modificar directamente
print(mi_tuple[4][0]) #Imprimir los datos dentro de otro dato
mi_tuple = list(mi_tuple)

t = (1,2,3,)
x,y,z = t #Se pueden asignar los valores del tuple a una variable siempre y cuando sean el mismo numero de variables de igual manera que en las listas
print(x,y,z)

y = (1,2,3,1)
print(len(y))
print(y.count(1)) #Metodo count ayuda a contar los valores dentro de una variable 
