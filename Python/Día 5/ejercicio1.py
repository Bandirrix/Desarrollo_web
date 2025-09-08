def devolver_distintos(num1, num2, num3):
    lista = [num1, num2, num3]
    lista.sort()
    print(lista)
    suma = 0
    for i in lista:
        suma += i
    if suma > 15:
       print(lista[2])
    elif suma < 10:
        print(lista[0])
    elif suma > 9 and suma < 16:
        print(lista[1])

devolver_distintos(0,10,9)  