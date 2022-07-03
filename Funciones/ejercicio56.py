""" import math

def cuadrado():
    base = float(input("Cual es la base del cuadrado?: "))
    altura = float(input("Cual es la altura del cuadrado?: "))
    if base <= 0 or altura <= 0:
        print("no se puede operar con numeros menores o iguales a 0")
    else: 
        global area_cuadrado
        area_cuadrado = base * altura
        return area_cuadrado

def circulo():
    radio = float(input("Cual es el radio del circulo? :"))
    if radio <= 0:
        print("No se puede efectuar la operacion con un radio {}".format(radio))
    else:
        global area_circulo
        area_circulo = 3.14 * (radio**2)
        return area_circulo

print(cuadrado())
print(circulo()) """

""" def Lista():
    nro = int(input("Cuantos elementos quieres en la lista? "))
    if nro <= 0:
        print("El nro debe ser mayor que 0")
    else:
        global lista
        lista = []
        while len(lista) < nro:
            lista.append(int(input("Pon un nro--> ")))
        return "la longitud de la lista es {}".format(len(lista))

print(Lista()) """

def medida(*tupla):
    print(len(tupla))

medida(2,3,4,10,20)