#Esto no era pero ahora entendí XD y no quiero borrar:
# n = int(input("Dame el nro de la tabla de multiplicar que quieres ver: "))
# for j in range(11):
# 	print("{} x {} = {}".format(n,j,j * n))

for i in range(1,11):
	for j in range(1,11):
		print(i*j, end="\t")
	print("")