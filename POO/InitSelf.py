""" class FabricaTelefono():
    marca = "Samsung"

    def ElaborarHuawei(self):
        #Self sirve para englobar un atributo a toda una clase
        self.marca = "Huawei"


telefono = FabricaTelefono()
telefono.ElaborarHuawei()
print(telefono.marca) """

#init

class FabricaTelefonos():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

telefono = FabricaTelefonos("Huawei", "Negro")
print(telefono.marca)
print(telefono.color)
