# *args viene del ingles argumentos, el cual es una abreviación de esta. Se pueda usar en las funciones para poder permitir una cantidad 
# arbitraria de valores sin llegar a tener un error
# con solo poner "*" antes de una palabra, esta ya es considerada como un argumento. el *hace alución a "todos los valores" 
'''
def suma (a,b):
    return a+b
                    Esta funcion da error debido a que el numero de argumentos es mayor a los permitidos
print(suma(5,6,4))
''' 
def suma(*args):
    total = 0
    for arg in args:
        total+= arg
    return total
 # la suma anterior se puede simplificar con la función "sum" de la siguiente manera: return sum(arg)
print(suma(5,4,5))
    
     