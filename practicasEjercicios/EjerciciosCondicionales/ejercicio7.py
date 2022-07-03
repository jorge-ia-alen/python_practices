# ammount = float(input("Cuanto dinero traes para aplicar un impositivo?: "))
# if ammount < 10000:
# 	tax = 5
# 	print("Tu tasa impositiva es del 5%, por lo cual el monto es de {}".format(ammount*tax/100))
# elif ammount > 9999 and ammount < 20000:
# 	tax = 15
# 	print("Tu tasa impositiva es del 15%, por lo cual el monto es de {}".format(ammount*tax/100))
# elif ammount > 19999 and ammount < 35000:
# 	tax = 20
# 	print("Tu tasa impositiva es del 20%")
# elif ammount > 34999 and ammount < 60000:
# 	tax = 30
# 	print("Tu tasa impositiva es del 30%, por lo cual el monto es de {}".format(ammount*tax/100))
# else: 
# 	tax = 45
# 	print("Tu tasa impositiva es del 45%, por lo cual el monto es de {}".format(ammount*tax/100))

#Codigo más optimo

# Preguntar al usuario por la renta
renta = float(input("¿Cuál es tu renta anual? "))
# Condicional para determinar el tipo impositivo dependiendo de la renta
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45
# Mostrar por pantalla el producto de la renta por el tipo impositivo
print("Tienes que pagar ", renta * tipo / 100, "€", sep='')