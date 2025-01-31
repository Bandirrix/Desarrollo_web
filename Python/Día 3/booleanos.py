# Los elementos del tipo booleano solo aceptan dos valores : True y false
# Se pueden declarar de manera directa o usando algun tipo de comparacion como > < >= <= == != ya que python hace la comparacion de la condicion 
# Tambien se puede obtener un valor booleano si se hace una consulta de si hay algo o no dentro de una variable

var1 = True
var2 = False
print(type(var1))
print(var2)

numero = 5> 2+3
print(type(numero))
print(numero) 

numero = 5== 2+3
print(numero)

numero = bool() #Genera un valor falso si no se pone nada dentro de los parentesis
print(numero)
numero = bool(5<4) #Otra manera de poder declarar valores booleanos
print(numero)

lista = [1,2,3,4]
control = 5 in lista #Preguntar si hay algo dentro de una variable 
print(type(control))
print(control)