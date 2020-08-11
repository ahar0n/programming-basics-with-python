# dos_mas_cercanos.py

x1 = float(input('x1: '))
y1 = float(input('y1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))
x3 = float(input('x3: '))
y3 = float(input('y3: '))

d12 = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
d13 = ((x3 - x1)**2 + (y3 - y1)**2)**(1/2)
d23 = ((x3 - x2)**2 + (y3 - y2)**2)**(1/2)

if d12 < d13 and d12 < d23:
    print('1 y 2 son los más cercanos.')
elif d13 < d12 and d13 < d23:
    print('1 y 3 son los más cercanos.')
else:
    print('2 y 3 son los más cercanos.')

# a(0,0), b(1,1), c(2,4)
# a(0,0), b(3,3), c(4,4)
# a(3,3), b(6,6), c(4,4)