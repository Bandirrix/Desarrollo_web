#  El formateo de cadenas ayuda cuando quieres usar diferntes tipos de datos dentro de la misma linea
# Se usa la función format que se usa poder decirle a python que en un espacio vacio será ocupado por una variable de
# un valor x.
# El uso de la función format es: print("Mi auto es {} y de matricula {}".format(color_auto, matricula))
# En esta manera lo que hace es que dejas los espacios donde estará ubicadas la variables, agregando format y las
# variables en el orden de los espacios.
# La manera "cadena literal" se hace un formateo más lineal: print(f"Mi auto es {variable} y de matricula {variable}")
# Esto se lee así: print para imprimir, con "f" indicas que se formateará la linea y entre llaves va la variable.
# Cuando usas la cadena literal, dentro de {} se usa el tipo de valor predeteminado de la entrada, como si pones un 3
# este será tomado de manera automatica como int.
x = 10
y = 5
# z = x+y

print("Mis numeros son " + str(x) + " y " + str(y))
print("Mis numeros son {} y {}".format(x,y))
print("Mis numeros son {} y {}".format(y,x))
print("La suma de {} y {} es igual a {}".format(x,y,x+y))

color = "rojo"
matricula = 123456
print(f"El auto es {color} y su matricula es {matricula}")