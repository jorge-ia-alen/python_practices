# n = int(input("Dame un nro entero positivo: "))
# while n > 0:
# 	print(n-1,end=", ")
# 	n-=1

#another way

n = int(input("Introduce un número entero positivo: "))
for i in range(n, -1, -1):
    print(i, end=", ")