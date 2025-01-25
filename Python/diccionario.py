# Un diccionario en python tiene valores claves que tiene valores unicos dentro de unas llaves
# Se escribe dentro de '{}'de manera que se pone la clave, separada por dos puntos y a su vez, separado por ',' por cada clave

diccionario = {'c1':'valor1','c2':'valor2'}
print(type(diccionario))
print(diccionario)
resultado = diccionario['c1'] #Busqueda de resultado de una clave se hace dentor de un corchete
print(resultado)

cliente = {'nombre':'Fernando','apellido':'Banda','peso':80,'altura':1.80}
consulta = cliente['altura']
print(consulta)

dic  = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}} #anidar diccionarios y listas
print(dic['c2'][0]) #Para buscar el dentro de una lista o dicc, se pone dentro de [] la clave y luego dentro de otros [] la sigiguinte clave o indice de la lista
print(dic['c3']['s1'])

dic2 = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic2['c2'][1].upper())

dic3 = {1:'a',2:'b'}
dic3[3] = 'c'
print(dic3)

dic3[2] = 'B'
print(dic3)

print(dic3.keys()) #Imprime las claves
print(dic3.values()) #Imprime los valores de las claves
print(dic3.items()) #Imprme las claves con los valores separados inidvidualmente


