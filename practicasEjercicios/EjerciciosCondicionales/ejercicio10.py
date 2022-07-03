# print("Tenemos pizza \n1.vegetariana y 2.no vegetariana: \n(Elija 1 o 2)")
# pizzaUsuario = int(input("Cual de las opciones quiere?: "))

# if pizzaUsuario == 1:
# 	preferencia = "vegetariana"
# 	ingredientes = input("Aquí tienes los sabores para elegir 'Tofu' y 'Pimiento': ")
# 	if ingredientes.lower() == "tofu":
# 		print("Genial!")
# 	elif ingredientes.lower() == "pimiento":
# 		print("Genial!")
# 	else:
# 		print("{} no existe".format(ingredientes))
# elif pizzaUsuario == 2:
# 	preferencia = "no vegetariana"
# 	ingredientes = input("Aquí tienes los sabores para elegir 'Peperoni', 'Jamón', 'Salmón': ")
# 	if ingredientes.lower() == "peperoni":
# 		print("Genial! {} entonces".format(ingredientes))
# 	elif ingredientes.lower() == "jamón" or ingredientes.lower() == "jamon":
# 		print("Genial! {} entonces".format(ingredientes))
# 	elif ingredientes.lower() == "salmón" or ingredientes.lower() == "salmon":
# 		print("Genial! {} entonces".format(ingredientes))
# 	else:
# 		print("{} no existe".format(ingredientes))
# else:
# 	print("{} no es una opción disponible".format(pizzaUsuario))

# print("Su preferencia es {} y sus ingredientes además del queso y el tomate son: queso, tomate y {}".format(preferencia,ingredientes))


print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")
# Decisión sobre el tipo de pizza
if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else: 
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetarina con mozarrella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")
