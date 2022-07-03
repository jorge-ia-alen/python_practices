class Recoger():
    def __init__(self):
        self._num1 = int(input("Ingrese el primer valor: "))
        self._num2 = int(input("Ingrese el segundo valor: "))

    def suma(self):
        return self._num1 + self._num2

    def resta(self):
        return self._num1 - self._num2

    def multiplicacion(self):
        return self._num1 * self._num2

    def division(self):
        if self._num1 < self._num2:
            print("El nro 2 es más grande que el nro 1, por lo tanto no puedo dividirlo")
        else:
            return self._num1 / self._num2

calcular = Recoger()
print(calcular.suma())
print(calcular.resta())
print(calcular.multiplicacion())
print(calcular.division())