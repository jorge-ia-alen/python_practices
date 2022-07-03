precio = input("Introduce un precio con sus respectivos sentimos(2): ")
print("Los euros son {} y los centavos son {}".format(precio[:precio.find(".")],precio[precio.find(".")+1:]))