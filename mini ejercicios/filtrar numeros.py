# Filtra números mayores a 10:

numeros = [5, 12, 8, 20, 3]

def filtrar(numeros):
    return[x for x in numeros if x>10]

print(filtrar(numeros))