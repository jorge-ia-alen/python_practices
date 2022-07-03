payasos = 112
munecas = 75

cantP = int(input("Cuantos payasos ha vendido en este paquete?: "))
cantM = int(input("Cuantas muñecas ha vendido en este paquete?: "))

op = (cantP*payasos) + (cantM*munecas)
print("El peso total del ultimo pedido vendido es: {} g".format(op))
