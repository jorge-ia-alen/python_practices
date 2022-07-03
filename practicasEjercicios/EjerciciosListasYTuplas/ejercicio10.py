# prices = [50, 75, 46, 22, 80, 65, 8]
# prices.sort()
# print("El menor es {} y el mayor es {}".format(prices[0],str(prices[-1:])))

prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
for price in prices:
    if price < min:
        min = price
    elif price > max:
        max = price 
print("El mínimo es " + str(min)) 
print("El máximo es " + str(max))
#Solucion que dio el profe, segun hiram la idea no eran usar funciones XDXDXDXD