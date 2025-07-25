def organizar_letras (palabra):
    lista = []
    for i in palabra: 
        lista.append(i)
    lista = set(lista)
    lista = list(lista)
    lista.sort()
    print(lista)

organizar_letras("perro")