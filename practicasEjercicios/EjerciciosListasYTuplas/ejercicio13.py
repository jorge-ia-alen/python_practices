numList = input("Ingresa los numeros separados por comas: ")
numList = numList.split(',')
n = len(numList)

for i in range(n):
	numList[i] = int(numList[i])
numList = tuple(numList)

sum, sumsq = 0,0

for i in numList:
	sum += i
	sumsq += i**2

mean = sum/n
stdev = (sumsq/n-mean**2)**(1/2)
print("La media es", mean, ", y la desviación tipica es ", stdev)