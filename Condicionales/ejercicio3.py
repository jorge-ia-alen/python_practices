""" rima1 = input("Dame la primera palabra: ")
rima2 = input("Dame la segunda palabra: ")


if rima1[-4:-1] == rima2[-4:-1]:
    print("Riman porque coinciden {} y {}".format(rima1[-4:-1], rima2[-4:-1]))
else:
    print("no riman") """

#Solucion del profe, mejor, tengo que practicar con las posiciones del array

palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

if len(palabra1) < 3 or len(palabra2) < 3:
    print("no rima porque tiene menos de tres caracteres")
elif palabra1[-3:] == palabra2[-3:]:
    print("Las palabras riman")
elif palabra1[-2:] == palabra2[-2:]:
    print("Las palabras riman")
else:
    print("las palabras no riman")