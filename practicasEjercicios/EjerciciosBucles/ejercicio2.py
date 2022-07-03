# age, i = int(input("Cuantos años tienes: ")),0
# while i <= age:
# 	print(i)
# 	i+=1

age = int(input("¿Cuantos años tienes?: "))
for i in range(age):
	print("Has cumplido " + str(i+1) + " años")