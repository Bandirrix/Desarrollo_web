# El uso de las kwargs hace refernecia al uso de argumentos en los cuales se pueden usar palabras clave como lo son en los diccionarios 
# De esta manera, al igual que los argumetos, puedes usar el numero de valores que tu quieras sin el riego de tener un error siempre que estos sean valores de tipo dict
# con solo poner "**" antes de una palabra, esta ya es considerada como un key word. el ** hace alución a "todos los valores", pero en cambio
# al tener valores de tipo diccionario, podemos utilziar también solo el valor o tambien la clave de cada item

def suma(**kwargs):
    print(type(kwargs))

def suma2(**kwargs):
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

def suma3(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor

    return total

def prueba(num1, num2, *args, **kwargs):

    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")



args = [100,200,300,400]
kwargs = {'x':'uno', 'y':'dos','z':'tres'}
suma(x=3, y=2, z=1)
suma2(x=3, y=2, z=1)
print(suma3(x=3, y=2, z=1))
prueba(1,1,2,2,3,4,5,x=2,y=3) #De esta manera, el codigo detecta el tipo y el orden del uso de argumentos definidos e indefinidos, por lo que hace que se use la funcion de manera correcta
prueba(5,10,*args,**kwargs) # Tambien lo que se puede hacer es crear una variable tipo lista o diccionario y agregar el * o ** para que sean tomados como argumentos indefinidos



