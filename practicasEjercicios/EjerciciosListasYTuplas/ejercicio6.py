materias,pasadas = ["Matemáticas", "Física", "Química", "Historia","Lengua"],[]
for i in range(len(materias)):
	nota = int(input("¿Qué nota has sacado en " + materias[i] + "?: "))
	if nota >= 5:
		pasadas.append(i)
for i in pasadas:
	materias.remove(i)
print("Las materias reprobadas son {}".format(materias))