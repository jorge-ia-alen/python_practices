""" nro1,nro2 = int(input("Dame el 1er nro: ")), int(input("Dame el 2do nro: "))

def comprobar():
    if nro1 > nro2:
        return 1
    elif nro1 < nro2:
        return -1
    else:
        return 0 

print(comprobar()) """

#funcion sobre el iva

cant = int(input("Cuantos elementos cargará? "))

def aplicarIva():
    iva = int(input("Cual es el porcentaje de iva a aplicar? "))
    listaPrecios = []
    if iva != 0:
        if iva > 0:
            for i in range(0, cant):
                precio = int(input("Cual es el precio del producto? "))
                precioFinalP = precio + ((precio*iva)/100)
                listaPrecios.append(precioFinalP)
                if i == 0:
                    precioTotal = precioFinalP
                else:
                    precioTotal = precioTotal + precioFinalP
        else:
            return "El iva es negativo"
    else:
        for i in range(0, cant):
            precio = int(input("Cual es el precio del producto? "))
            precioFinalP = precio + ((precio*21)/100)
            listaPrecios.append(precioFinalP)
            if i == 0:
                precioTotal = precioFinalP
            else:
                precioTotal = precioTotal + precioFinalP

    return "El precio final es {}\nLos precios finales individuales son {}".format(precioTotal,listaPrecios)

print(aplicarIva())