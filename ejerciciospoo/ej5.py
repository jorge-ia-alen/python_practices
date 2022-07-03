""" class Universidad():
    def recon(self):
        print("Universidad Paraguayo Alemana de Ciencias Aplicadas")

class Carrera(Universidad):
    def reconc(self):
        print("Business Informatics")

class Estudiante(Carrera):
    def ident(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


persona = Estudiante()
persona.ident("Jorge", 20)

print(persona.nombre)
print(persona.edad) """

class Universidad():
    def __init__(self,Nombre):    self.Nombre = Nombre

class Carerra():
    def carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carerra):
    def datos(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad
        print("Mi nombre es {}, tengo {} años. mi especialidad es {}. Estudio en la Univerdad {}".format(self.nombre,self.edad, self.especialidad, self.Nombre))

persona = Estudiante("Paraguayo Alemana")
persona.carrera("Business Informatics")
persona.datos("Jorge Cabral", 20)

