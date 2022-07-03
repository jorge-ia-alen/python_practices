n = int(input("Dame un nro para la altura del triangulo rectangulo: "))
for i in range(n):
	for j in range(i+1):
		print("*", end="")
	print("")