# Para poder hacer uso de las clases en Python, se usa la palabra reservada "class", seguido por el nombre de la clase 
# En los nombres se empienza con mayuscula y se omiten los espacios. Lo que se hace es en cada palabra se empieza con mayuscula 

class pajaro: #Declaración del objeto
    pass      #Pass se pone para poder crear la instancia sin necesidad de declarar nada dentro del objeto

mi_pajaro = pajaro() #Instancia creada con el objeto pajaro, a una variable le asignas el objeto pajaro
print(type(mi_pajaro))
#  Cualquier tipo de objeto creado en el codigo es considera un nuevo tipo de variable 
print(mi_pajaro)
otro_pajaro = pajaro()
print(otro_pajaro)
 