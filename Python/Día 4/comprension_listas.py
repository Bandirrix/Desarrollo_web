# 

palabra = 'python'
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)

lista = [letra for letra in 'python'] # Esto se puede leer como que vas a agregar el valor de letra por cada valor en la palabra python 
lista2 = [n for n in range(0,21,2)] # Esto se puede leer como que vas a agregar el valor de n por cada numero en el rango  
print(lista2 )

lista2 = [n/2 for n in range(0,21,2)] # Esto se puede leer como que vas a agregar el valor de n por cada numero en el rango (Se puede hacer operaciones dentro de la sentencia) 
print(lista2 )

lista3 = [n if n *2 > 10 else 'no' for n in range(0,21,2)] # Agregar un numero si n * 2 es mayor a 10, si no. pon 'no' por cada valor en el rango
print(lista3)

pies = [10,20,30,40,50]
metros = [p/3.281 for p in pies]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [valor for valor in valores if valor%2 == 0]