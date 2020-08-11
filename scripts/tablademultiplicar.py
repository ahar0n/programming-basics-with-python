# tablademultiplicar.py
n = int(input('ingrese número: '))
for i in range(10):
    print('{:5} x {} = {}'.format(i+1, n, n*(i+1)))