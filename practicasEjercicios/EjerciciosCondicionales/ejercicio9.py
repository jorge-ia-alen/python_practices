# edadCliente = int(input("Cual es tu edad?: "))
# if edadCliente < 4:
# 	print("Usted entra gratis")
# elif edadCliente > 4 and edadCliente < 18:
# 	print("Usted paga 5 Euros")
# elif edadCliente > 17:
# 	print("Usted paga 10 Euros")
# else:
# 	print("No entiendo")

#Otra solucion, más optima, mismo resultado
edad = int(input("Introduce tu edad: "))
# Decisión del precio en función de la edad
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 4
else:
    precio = 10
# Mostrar precio
print("El precio de la entrada es", precio, "€.")