eleccion = input("Elija uno de los siguientes candidatos: \nA. Rojo\nB.Verde\nC.Azul\n:")

if eleccion.lower() == "a":
    print("usted ha votado por el partido Rojo")
elif eleccion.lower() == "b":
    print("usted ha votado por el partido verde")
elif eleccion.lower() == "c":
    print("usted ha votado por el partido azul")
else:
    print("Opción Erronea")

