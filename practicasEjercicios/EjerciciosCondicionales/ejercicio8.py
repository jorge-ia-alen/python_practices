# puntosUsuarios = float(input("Cuantos puntos tienes?(Solo valen de 0.2, 0.4 y así de 2 en 2: "))

# if (puntosUsuarios*10) % 2 == 0:
# 	if puntosUsuarios < 0.4:
# 		print("Tu nivel es Inaceptable, maldita lagartija! como solo {} puntos?, tus BENEFICIOS SON {}".format(puntosUsuarios, 2400*puntosUsuarios))
# 	elif puntosUsuarios < 0.41:
# 		print("Tu nivel es Aceptable, tus beneficios son {}".format(0))
# 	elif puntosUsuarios > 0.59:
# 		print("Tu nivel es Meritorio, tus beneficios son {}".format(2400 * puntosUsuarios))
# 	else:
# 		print("No sé que pasa aca")
# else:
# 	print("El numero {} no es correcto".format(puntosUsuarios))

#Otra forma

bonificacion,inaceptable,aceptable,meritorio = 2400,0,0.4,0.6
puntos = float(input("Introduce tu puntuación: "))
# Clasificación por niveles de rendimiento
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""
# Mostrar nivel de rendimiento
if nivel == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))