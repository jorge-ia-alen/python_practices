n = int(input("Introduce un nro para el dividendo: "))
m = int(input("Introduce un nro para el divisor: "))

c,r = n/m, n%m

print("El cociente de la división es {} y el resto de la división es {}".format(c,r))