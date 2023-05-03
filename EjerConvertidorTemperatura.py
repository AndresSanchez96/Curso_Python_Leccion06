print('Convertidor de temperatura')
def Fahrenheit(grados):
    total = (9/5) * grados + 32
    return total

def celsius(fahren):
    total1 = (5/9) * (fahren-32)
    return total1

des = int(input('Si desea transformar de Celsius a Fahrenheit marque 1 \n'
                'Si desea transformar de fahrenheit a Celsius marque 2: '))
if des == 1:
    grados = float(input('Digite el valor en Celsius: '))
    print(f'El valor {grados} grados Celsius corresponde a: {Fahrenheit(grados)}'
          f' grados Fahrenheit')
elif des ==2:
    fahren = float(input('Digite el valor en Fahrenheit: '))
    print(f'El valor {fahren} grados Fahrenheit corresponde a: {celsius(fahren)}'
          f' grados Celsius')
else:
    print('Valor incorrecto ')