#Las variables pueden almacenar y sobreescribir los datos sin sin ningun tipo de restriccion
# Casting se le denomina a la conversion de datos y hay dos tipos: Implicitos y explicitos.
# Los implicitos son los que automaticamente son interpretados por python con un tipo de dato especifico
# Los explicitos son los datos que el usuario necesita elegir que tipo de dato usará

num1 = 20
num2 = 30.5
print(type(num1))
print(type(num2))
num1 = num2 + num1
print(type(num1))
print(type(num2))

num3 = 5.8
print(num3)
print(type(num3))
num4 = int(num3) # Esta es la manera para poder convetir el tipo de dato que tenemos
print(num4)
print(type(num4)) #El numero float al hacerlo entero, eliminia el punto decimal dejando solo el entero, pero no lo
                  # redondea

edad = input("Dime tu edad: ")
print(type(edad))
edad = int(edad)
nueva_edad = 1 + edad
print("Tu nueva edad será: " + nueva_edad) #Aquí salta un error porque no deja concatenar int con str
print(type(nueva_edad))