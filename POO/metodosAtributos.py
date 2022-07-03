class FabricaTelefonos():
    marca = "Huawei"
    color = "Negro"
    ram = 32
    rom = 128

    #metodo de instancia (que creamos)
    def llamar(self, mensaje):
        return mensaje

    def escucharMusica(self):
        print("Estas escuchando musica")




telefono = FabricaTelefonos()
print(telefono)
telefono.marca
telefono.color
telefono.ram
telefono.rom

print(telefono.ram)

print(telefono.llamar("Hola, Con quien hablo?"))
telefono.escucharMusica()
