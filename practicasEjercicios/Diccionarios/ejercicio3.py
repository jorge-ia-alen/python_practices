frutas = {"Platano": 1.35, "Manzana":0.80, "Pera": 0.85, "Naranja": 0.70}
fruta, peso = input('Que fruta quiere llevar?: '), float(input('Cuantos kilos de fruta llevara?: '))
fruta = fruta.capitalize()
if fruta not in frutas:
	print('No tenemos {} en existencia'.format(fruta))
else:
	print('{} esta a {} el kilo, el total a facturar es {:.2f} $'.format(fruta,frutas[fruta],frutas[fruta]*peso))