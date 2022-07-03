""" while True:
    try:
        num1 = int(input("Ingresa un nro: "))
        resultado = 100/num1
        print(resultado)
        break
    except ZeroDivisionError:
        print("No se puede dividir entre 0") """

""" while True:
    try: 
        edad = int(input("Ingresa tu edad: "))
        print("Tu edad es: ", edad)
        break
    except ValueError: 
        print("Has colocado un valor erroneo") """


while True:
    try:
        edad = int(input("ingresa tu edad: "))
        print("Tu edad es: ", edad)
        break
    except KeyboardInterrupt:
        print("\nNo me interrumpas carajo")
        break