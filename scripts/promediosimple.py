i = 1
suma = 0
n = input('ingrese nota {}: '.format(i))
while n != 'x':
    suma += float(n)
    i += 1
    n = input('ingrese nota {}: '.format(i))
print('El promedio es {}'.format(suma/(i-1)))

