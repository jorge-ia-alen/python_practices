# fecha = input("Dame tu fecha de nacimiento separado por '/': ")
# dia = fecha[:2]
# mes = fecha[3:5]
# anho = fecha[6:]
# print("el día es {} el mes es {} y el año es {}".format(dia, mes, anho))

# Second case:

fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)