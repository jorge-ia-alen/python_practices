class Fabrica():
    def __init__(self, llantas, *color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    #Llantas
    @property
    def llantas(self):
        return self._llantas

    @llantas.setter
    def llantas(self,llantas):
        self._llantas = llantas
    #color
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,*color):
        self._color = color
    #precio
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self,precio):
        self._precio = precio


class Auto(Fabrica):
    pass

class Moto(Fabrica):
    pass

print("\n")
auto = Fabrica(4, 'rojo', 'azul', 'verdad', 'rosa', precio = 12000)
print("El auto tiene {} ruedas, los colores para elegir son: \n{} \nY cuesta {} USD".format(auto.llantas, auto.color, auto.precio))

moto = Fabrica(2, 'rojo', 'azul', 'verdad', 'rosa', 'violeta', precio = 2000)
print("\n")
print("La moto tiene {} ruedas, los colores para elegir son: \n{} \nY cuesta {} USD".format(moto.llantas, moto.color, moto.precio))