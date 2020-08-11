# division.py algoritmo que, a partir de los números dividendo y el divisor, calcula
# y muestre la división y el cociente. Además, muestra si la división es exacta o no. 
# En el caso que la división no sea exacta, muestra el resto.

dividendo = int(input('Dividendo: '))
divisor = int(input('Divisor: '))

cociente = dividendo // divisor
resto = dividendo % divisor

print(f'{dividendo}/{divisor} = {cociente}')
if resto != 0:    
    print(f'La división no es exacta, el resto es {resto}')
else:
    print('La división es exacta')