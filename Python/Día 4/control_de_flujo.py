#Condicionantes IF - toma de decisiones
# Srgun se cumpla una condicion, python debe de tomar una decision con respecto a esta para poder continuar con el codigo
# If es igual a un "si" pasa esto > if una_condicion
# Elif es parecido pero significa "si no pasa esto, que pase esto otro" y pueden haber tanto como quieras, ya que esta lo hace es si no se 
# cumple la condición inicial, va ir de una en una de las elif hasta agotar las opciones 
# Else "sino" una condicion final si no se cumple ninguna condición 
### Aqui lo que es importante es la identacion del codigo, ya que es lo que rige las opciones de prioridad de python

if 10 > 9:
    print('Es correcto')
if True:
    print('Esto también es correcto')

if 5==2:
    print('Es correcto')
else:
    print('Esto no es correcto')

mascota = "toro"
if mascota == "gato":
    print("Usted efectivamente tiene un gato")
elif mascota == "toro":
    print("Como es que conseguiste un toro??")  #La condición elif te permite incorporar otra condición para poder seguir evaluando
elif mascota == "perro":
    print("Que bonito, tienes un perrito")
else:
    print("La verdad es que no sé que mascota tienes")

edad = input("Que edad tienes?? ")
edad = int(edad)

if edad < 18:
    print("Eres menor de edad")
    calificacion = int(input("Cual es la calificación de tu ultimo parcial?? ")) #Se puede anidar condicionantes siempre y cuando se respete la identacion
    if calificacion >= 7:
        print("Eres inteligente y aprobaste")
    else:
        print("Echele ganas mijo")
else:
    print("Eres ya todo un adulto")
