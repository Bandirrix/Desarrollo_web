# Si bien las funciones no devuelven un valor por si solas, el objeto return ayuda a que un valor obtenido dentro de una función pueda ser 
# almacenado dentro de una variable con el fin de poder obtener algo de esta y poder darle una utilidad

def multipicacion (num1, num2):
    return num1 * num2

print(multipicacion(5,10))
resultado = multipicacion(5,10)
print(resultado)

def multi (num1, num2):
    total = num1 * num2 # Este caso es relativamente diferente ya que se hizo el proceso de una multiplicación dentro de una variable interna, no directamente en el return, pero el resultado es completamente igual
    print(total) # Aqui también se puede hacer uso de un print para que al usar la funcion automaticamente este sea mostrado en pantalla
    return total

resul = multi(10,10)


# La diferncia entre usar un print a un return es que al usar solo print, la info muere automaticamente luego de ejecutar la linea, y con return es posible almacenarla

