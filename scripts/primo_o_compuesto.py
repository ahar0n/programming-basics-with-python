# primo_o_compuesto.py
numero = int(input('Ingresa un número: '))
divisor = numero - 1
divisibles = 0
while divisor > 1:
    if numero%divisor == 0:
        divisibles += 1
    divisor -= 1
if divisibles > 0:
    print('Es compuesto')
else:
    print('Es primo')