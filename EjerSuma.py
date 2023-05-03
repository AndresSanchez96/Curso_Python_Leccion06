def suma(*args):
    resultado = 0
    # iteramos
    for i in args:
        resultado += i
    return resultado

print(suma(3,5,9))