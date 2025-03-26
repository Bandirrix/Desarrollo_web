# En el ciclo while se repite una acción mientras se cumpla una condición especifica.
# Usando este ciclo podemos  repetir una de una manera más dinamica
# Si no se especifica bien en que punto debe de terminar el ciclo, este se ejecutará sin fin hasta cerrar el programa o apagar la compu
# Se puede hacer uso de un else para cuando la condición ya no se cumpla
# A diferencia del bucle for, en este el numero de iteracion pueder ser arbitraria dependiendo el comportamiento del usuario, y no es tan predictivo como el FOR 

monedas = 5
while monedas > 0: 
    print(f"Tengo {monedas} monedas")
    monedas -= 1 #Esta es la condicion que va decreciendo el valor de la variable original para poder romper el ciclo. Esta es una manera tambien para poder indicar que reste una cantidad especifica
else:
        print("No tengo más monedas")

respuesta = "s"
while respuesta == "s":
      respuesta = input("Quieres seguir? (s/n)")
else:
      print("Gracias, ya quería descansars")

respuesta = "s"
while respuesta == "s":
      pass #La función de PASS es para poder dejar un aparte del codigo y que se la pueda saltar sin que arroje problemas
print("Luego regreso aquí")

nombre = input("Tu nombre:")
for letra in nombre:
      if letra == "r":
            break # Break puede romper el bucle si se cumple la condición
      print(letra)

nombre = input("Tu nombre:")
for letra in nombre:
      if letra == "r":
            continue # continue puede continuar el ciclo si se cumple la condicion, solo que salta la iteración donde esta es verdadera
      print(letra)