# Con ZIP lo que puedes hacer es unir dos o más listas coleccionables en una serie de tupples dentro de una lista.
# Esto se hace especificando cuales serán las listas a usar para hacerlo

nombre = ['Ana', 'Hugo', 'Valeria']
edades = [65,32,16]

combinados = list(zip(nombre,edades)) #Aquí es necesario hacer el cambio de tipo de variable a lista, ya que si no lo hacemos, solo aparece que sí existe un obejto zip
print(combinados)

nombre = ['Ana', 'Hugo', 'Valeria', 'Luis']
edades = [65,32,16]

combinados = list(zip(nombre,edades)) #Aqui no cambia nada debido a que la función zip toma como valor nominal la lista que contenga menos elementos.
print(combinados)

nombre = ['Ana', 'Hugo', 'Valeria', 'Luis']
edades = [65,32,16]
ciudades = ['México','México','México']
combinados = list(zip(nombre,edades,ciudades)) #Se puede hacer zip de varios coleccionables de datos
for nombre,edades,ciudades in combinados:
    print(f"{nombre} tiene {edades} años y vive en {ciudades}")

