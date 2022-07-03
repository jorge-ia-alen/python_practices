#self puede ser cualquier otro nombre siempre y cuando se sepa su funcion
class FabricaTelefonos(): 
    def __init__(self, marca, *colores, **modelos):
        self.marca = marca
        self.colores = colores
        self.modelos = modelos

telefono = FabricaTelefonos("Alcatel", "Negro", "Azul", "Rojo",m1 = 500, m2 = 1000)
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)
telefono.memoria = 512
print(telefono.memoria)