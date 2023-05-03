def multiplicacion(*args):
    resultado = 1
    for i in args:
        resultado *= i
    return resultado

print(f'La multiplicacion es: {multiplicacion(3,5,7)}')