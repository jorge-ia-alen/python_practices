age, ammount = int(input("Cual es tu edad?: ")), float(input("Cuanto dinero ganas por mes?: "))
if age > 15: 
	if ammount > 999:
		print("Tienes {} y puedes tributar ya que tus ingresos son {}".format(age, ammount))
	else:
		print("Tienes {} pero tus ingresos no superan los 1000 Euros, entonces no debes tributar".format(age))
else: 
	if ammount > 999:
		print("Tienes {} y superas los 1000 Euros, pero aun así no debes tributar por tu edad".format(age))
	else: 
		print("No tienes la edad y tampoco superas el monto establecido para tributar")


#Esta manera era más sencilla
# age = int(input("¿Cuál es tu edad? "))
# income = float(input("¿Cuales son tus ingresos mensuales?"))
# if age > 16 and income >= 1000:
#     print("Tienes que cotizar")
# else:
#     print("No tienes que cotizar")