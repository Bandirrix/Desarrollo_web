# Con la palabra enumerate podemos darle un indice a una lista de valores, obteniendo como resultado un tupple 

lista = ['a','b','c']
indice = 0 

for item in lista:
    print(indice,item)
    indice += 1

lista2 = ['a','b','c']
for a,i in enumerate(lista): #Esto hace que el primer valor obtenido sea el indice, al generarse un tupple, y el segundo sea el valor
    print(a,i)

palabra = list("Python") #Con esto haces casting de la palabra a lista
print(palabra)
lista_indices = list(enumerate(palabra)) #Con esto haces casting de las tupples que te genera al usar enumarate para meterla en unsa lista
print(lista_indices)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for a,i in enumerate(lista_nombres):
    if i.startswith("M") == True:
        print(a)