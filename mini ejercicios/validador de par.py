# Crea una función que reciba un número y diga si es par o impar.

def parImpar(n):
    if n % 2 == 0:
        return f"{n} es par"
    else: 
        return f"{n} es impar"
    
print(parImpar(7))

# Ejecuta: py 'validador de par.py'