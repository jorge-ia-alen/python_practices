class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Yo hago Guau!")


class Pez(Animales):
    def hablar(self):
        print("Yo hago glu glu glu")

perro = Perro("Guau")
perro.hablar()

animal = Animales("Miau")
animal.hablar()

pez = Pez()
pez.hablar()