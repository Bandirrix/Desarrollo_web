def contar_primos(numero):
    lista = []
    lista = list(range(numero+1))
    print(lista)

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5)+1):
        if numero % i == 0:
            return False
    return True


contar_primos(20)