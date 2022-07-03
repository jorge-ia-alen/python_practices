#como yo lo hice
# palabra = input("Dame una palabra: ")
# longWord = len(palabra)
# while longWord > 0:
# 	print(palabra[longWord-1])
# 	longWord-=1

#como lo hizo el dueño de la pagina
word = input("Introduce una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])