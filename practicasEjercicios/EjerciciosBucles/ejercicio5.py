# inversion,interes,anhos,result = float(input("Cuanto va a invertir?: ")), float(input("Cuanto es el interes anual?: ")),int(input("Cuantos años dura la inversión: ")),0
#inversión y luego que, almacenamos en una variable lo que es de un año y luego el resto en otra nueva que se ira imprimiendo hasta el final
# for i in range(anhos):
# 	if i == 0:
# 		result = inversion + ((inversion*interes)/100)
# 		print("El resultado de la inversión en el año {} es {}".format(anhos,result))
# 	elif i < anhos:
# 		result = result+((result*interes)/100)
# 		print("El resultado de la inversión en el año {} es {}".format(anhos,result))
# 	else: 
# 		print("O ya se termino el ciclo o hay un error")


# otra manera de hacer el codigo
amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
for i in range(years):
    amount *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))