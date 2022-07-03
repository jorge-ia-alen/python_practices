# userName,gender = input("Cual es tu nombre?: "), input("Cual es tu genero (Solo vale M o F): ")
# womenList, menList = "aAbBcCdDeEfFgGhHiIjJkKlLmM", "nNoOpPqQrRsStTuUvVwWxXyYzZ"

# validator = str(userName[0])

# if gender == "M" and validator in menList:
# 	print("Usted {} pertenece al grupo A".format(userName))
# elif gender == "M" and validator not in menList:
# 	print("Usted {} pertenece al grupo B".format(userName))
# elif gender == "F" and validator in womenList:
# 	print("Usted {} pertenece al grupo A".format(userName))
# else:
# 	print("Usted {} pertenece al grupo B".format(userName))


#Me olvide que python también tiene el abecedario XD, 2hs al pedo

name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")
if gender == "M":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)