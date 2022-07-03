import math

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))

""" op = b^2 - 4*a*c
r = math.sqrt(op)
result1 = (-b + op)/2*a
result2 = (-b - op)/2*a
print(result1 + '\t', result2) """

x1 = 0
x2 = 0

if ((b**2)-(4*a*c )) < 0:
    print("No se puede realizar porque es un nro negativo")
else: 
    x1 = (-b + math.sqrt((b**2)-(4*a*c)))/(2*a)
    x2 = (-b - math.sqrt((b**2)-(4*a*c)))/(2*a)


print("La solución es: \nx1=",x1, "\nx2=",x2)