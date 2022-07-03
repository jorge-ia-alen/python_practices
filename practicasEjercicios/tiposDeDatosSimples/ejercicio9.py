inversion = int(input("Cuanto capital desea invertir?: "))
interes = int(input("Cuanto es el interes anual de su inversión?(Pon un nro entero): "))
plazo = int(input("Cuantos años dejará el capital?: "))

roi = (inversion *(interes/100+1) ** plazo)

print("Las ganancias obtenidas en su inversión son: {0:.2f}".format(roi))