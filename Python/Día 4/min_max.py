# Estos atributos nos sirven para poder saber el valor mas alto o el más bajo en una coleccion de datos, y estos no solo son para valores numericos

menor = min (10,25,98,35,62)
print(menor)
mayor = max (10,25,98,35,62)
print(mayor)
lista = [10,25,98,35,62]
print(f"El menor es {min(lista)}, y el mayor es {max(lista)}")

nombres = ['Luis','Valeria','Fernando','Lizette'] #Busca por la primer letra "min" o la mayor "max"
print(min(nombres))
nombre = 'Fernando'
print(min(nombre)) #Con este metodo, contempla lo que primero las letras mayusculas y luego las letras en orden alfabetico

dic= {'C1':45,'C2':11}
print(min(dic)) #Busca en base a las claves

dic= {'C1':45,'C2':11}
print(min(dic.values())) #Si prefieres buscar en lugar de eso por los valores, lo que hay que hacer es poner el .value  