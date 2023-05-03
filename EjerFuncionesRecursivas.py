def imprimir(numero):
    if numero >= 1:
        print(numero)
        imprimir(numero-1)
    elif numero < 0:
        print('Valor incorrecto')

imprimir(int(input('Digite numero: ')))
