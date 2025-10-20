def invertirEntero(n):
    if type(n) != int or n < 1:
        raise Exception("n debe ser entero positivo.")
    return invertirEnteroAux(n)

def invertirEnteroAux(n):
    if n < 10:
        return n
    else:
        return (n % 10) * 10**contarDigitos(n // 10) + invertirEnteroAux(n // 10)

def contarDigitos(n):
    if n < 10:
        return 1
    else:
        return contarDigitos(n // 10) + 1

# Ejemplo de ejecución
numero = 12345
resultado = invertirEntero(numero)
print("Número invertido:", resultado)
