# multiplosdedosentredos.py muestra numeros pares entre dos numeros ingresados
# constraint: n1 < n2
a = int(input('a: '))
b = int(input('b: '))
while a < (b-1):
    a += 1
    if a%2 == 0:
        print(a)