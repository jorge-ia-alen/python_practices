a, b,product = ((1,2,3),(4,5,6)), ((-1,0),(0,1),(1,1)), [[0,0],[0,0]]

for i in range(len(a)):
	for j in range(len(b[0])):
		for k in range(len(b)):
			product[i][j] += a[i][k] * b[k][j]

for i in range(len(product)):
	product[i] = tuple(product[i])
product = tuple(product)

for i in range(len(product)):
	print(product[i])

#No todo fue propio, pero aun trato de entender como no funciono solo con dos contadores.
#Ahora lo explico un poco, al el primer for el len de a es 2, en el segundo el len de b[0] es dos también, y en el tecer for es len de b es 3, entonces esta contando para el la fila i en el elemento j que se contará 2 veces o sea primera y segunda columna es igual a la multiplicación de a[fila 0][contador de la los elementos dentro de la fila] * b[contador de la fila][contador de los elementos de la fila] que no va a superar el nro 2, entonces esta haciendo bien su trabajo

#En si lo que quiero saber, porque no puedo solo hacerlo en dos lineas. porque el nro o superaria los elementos o no le alcanzaría, se requiere el orden para poder contar de esa manera los elementos y multiplicar los correspondientes, sino estaría teniendo operaciones vacias o muchos errores. A continuacion se convierte en una tupla ya que son como una lista o algo así de tal manera a concretar el ejercicio de tuplas xd. 