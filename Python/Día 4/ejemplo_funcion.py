precio_cafe = [('capucciono',50),('moka',55),('americano',45)]

def cafe_mas_caro (lista_precios):

    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe,precio in lista_precios: # Se hace una doble definicion de variables ya que se quiere revisar las dos partes del tupple, se asigna el tipo de bebida la priner valor y el costo al segundo
        if precio > precio_mayor:
            precio_mayor = precio # Se sobreescribe el valor del precio en cada vuelta evaluado por la condición
            cafe_mas_caro = cafe # Se sobreescribe el nombre de la bebida en cada vuelta evaluado por la condición
        else:
            pass
    return (cafe_mas_caro,precio_mayor) # Devuelve un tupple 

cafe,precio = cafe_mas_caro(precio_cafe) # Define dos variables en las cuales se guardará el return de la función, ña cual es un tupple 
print(f'El café más caro es el {cafe} con un valor de {precio}')