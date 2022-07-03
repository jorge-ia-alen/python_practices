nro = int(input("Dame un nro cualquiera: "))

if nro > 0:
    print("El valor absoluto del nro es: ", nro)
else:
    nro = nro * -1
    print("El valor absoluto del nro es ", nro)


if nro > 0:
    print("El valor absoluto del nro es: {}".format(nro))
else:
    print("El valor absoluto del '{}' es {}".format(nro,abs(nro)))
