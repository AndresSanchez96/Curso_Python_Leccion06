
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

numero = int(input('Digite un numero: '))
print(f'El factorial de {numero} es : {factorial(numero)}')