# Los operadores logicos son "y", "o" y "no". And, or y not
# Al usarse "AND" hace una doble comparación, en la cual, si una de las dos no es verdad, es FALSE
# "Or" también es para doble comparación, pero aquí es si no se cumple una puede ser la otra. Si ninguna se cumple, es FALSE, si al menos una se cumple, es TRUE
#"Not" hace un cambio del valor booleano de una comparación

mi_bool = (4<5) and (5 == 2+3) # Las comparaciones se pueden separar por parentesis
print(mi_bool)
mi_bool = (4<5) and ('perro' == 'perro') #Se pueden hacer dobles comparaciones con diferentes tipos de datos
print(mi_bool)
mi_bool = (4 == 5) or (3 == 2+3) #Comparación usando operaciones
print(mi_bool)
texto = "este es una frase breve"
mi_bool = ('frase' in texto) or ('python' in texto) #Comparación de busqueda de texto en
print(mi_bool)
mi_bool = not ('a' == 'a')
print(mi_bool)
