# Crea una lista con 5 números y muestra el doble de cada uno.

def dobles(lista):
    resultado = []
    for item in lista:
        resultado.append(item*2)
    return resultado

print(dobles([1,2,3,4,5]))

def dobles(lista):
    return [item*2 for item in lista]

print(dobles([2,4,6,7,8]))