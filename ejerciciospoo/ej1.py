class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

        if nota < 6:
            print("Estudiante {} Reprobado por imbecil".format(nombre))
        elif nota > 5 and nota < 10:
            print("Estudiante {} Aprobado".format(nombre))
        else: 
            print("La nota {} no se puede considerar".format(nota))

estudiante = Estudiante("Jorge", 5)