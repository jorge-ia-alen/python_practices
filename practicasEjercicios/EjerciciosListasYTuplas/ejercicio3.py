materias,notas = ["Matemáticas", "Física", "Química", "Historia","Lengua"],[]
for i in range(len(materias)):
	nota = input("¿Qué nota has sacado en " + materias[i] + "?: ")
	notas.append(nota)
for i in range(len(materias)):
	print("Tu nota en {} es {}".format(materias[i],notas[i]))