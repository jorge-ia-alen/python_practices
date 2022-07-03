# nombre = input("Cual el nombre del producto?: ")
# precio = float(input("Cual es el precio del producto?: "))
# unidades = int(input("Cuantos unidades tienes del producto?: "))

# arr = [nombre, precio, unidades, precio*unidades]
# print(arr)

producto = input('Introduce el nombre del producto: ')
precio = float(input('Introduce el precio unitario: '))
unidades = int(input('Introduce el número de unidades: '))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))