# Con el objeto 'def', el cual significa definicion, puedes crear un una funcion con lines de codigo que ejecuten una accion especifica y que puede ser repetible las veces que sea necesario
# Es 'def' seguido del nombre de la función (este es un nombre arbitrario) + dos () y + ':'
# Lo que indican los dos puntos es que lo que sigue despues es el codigo de la función y esta debe de estar identada para tomarse en cuenta 
# Luego, dentro de la función se suele poner 3 ''' descripción de lo que hace la función y luego 3 ''' para cerrarlo
# Dentro de los parentesis lo que nosotros podemos hacer es pasar parametros especificos que trabajan internamente en la función

def saludar_persona (nombre):
    ''' 
    Esta función sirve para saludar a las personas
    Con las 3 comillas puedes hacer comentarios multilinea
    '''
    print('Hola ' + nombre)

saludar_persona('Fernando')