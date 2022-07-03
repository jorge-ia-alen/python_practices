# Code by me
# correo = input("Dame tu correo electronico: ")
# i = 0
# while i < len(correo):
# 	if correo[i] == "@":
# 		mail = correo[0:i]

# 	i+=1

# print("Tu correo modificado es: {}@ceu.es".format(mail))

#Code by the professor:
email = input("Introduce tu correo electronico: ")
print(email[:email.find('@')]+'@ceu.es')