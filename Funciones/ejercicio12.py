""" lista,nro,cont=[],0,0
nro = int(input("Cuantos nros quieres en la lista?: "))

while len(lista) < nro:
    lista.append(int(input("Pon un nro aquí --> ")))

def parImpar():
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)

    print("La lista es {} \nLos pares son {}\nLos impares son {}".format(lista,pares,impares))


parImpar() """

#factorial

""" def factorial():
    nro = int(input("Nro para factorial --> "))
    if nro > 0:
        factorial = 1
        for i in range(1,nro+1):
            factorial = factorial * i
        print(factorial)            
    else:
        print("El nro es negativo y no podemos proceder")

factorial() """





def factorial():
    from math import factorial
    num = int(input("Ingresa nro: "))
    if num > 0:
        print(factorial(num))
    else:
        print("El nro es negativo")

factorial()
