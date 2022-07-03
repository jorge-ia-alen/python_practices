practica1 = float(input("Ingrese el valor de la practica 1: "))
practica2 = float(input("Ingrese el valor de la practica 2: "))
practica3 = float(input("Ingrese el valor de la practica 3: "))
ExamenParcial = float(input("Ingrese el valor del examen parcial "))
ExamenFinal = float(input("Ingrese el valor del examen Final "))

pp = (practica1 + practica2 + practica3)/3

promedioFinal = (pp + 2*ExamenParcial + 3*ExamenFinal)/6

print("El promedio de las practicas del estudiantes es: ", pp,"\nEl promedio final del estudiantes es: ", promedioFinal)