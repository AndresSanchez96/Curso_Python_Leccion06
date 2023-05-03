print('Calculadora de impuestos ')
def calculadora(pago,impuesto):
    pago_total = pago + pago*(impuesto/100)
    return pago_total

pago = float(input('Digite el valor del pago: $'))
impuesto = float(input('Digite el valor del impuesto (%)'))
print(f'El valor total con impuesto incluido es de: {calculadora(pago,impuesto)}')