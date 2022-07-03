peso = float(input("Cuanto pesas en kg?: "))
altura = float(input("Que tan alto eres en m?: "))

imc = peso/(altura**2)

print("Tu indice de masa corporal es {0:.2f}".format(imc))