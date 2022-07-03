diccionario = {}
palabras = input("Introduce las palabras que quieres agregar separadas ':' y separada por comas: ")
for i in palabras.split(','):
	clave,valor = i.split(':')
	diccionario[clave] = valor
frase = input('Introduce una frase en espanhol: ')
for i in frase.split():
	if i in diccionario:
		print(diccionario[i], end=' ')
	else:
		print(i,end=' ')

#Codigo de marcelo
# from sys import argv
# script, first, second, third = argv,argv,argv,argv

# print('the script is called: ', script)
# print('Your first variable is: ', first)
# print('Your second variable is: ', second)
# print('Your third variable is: ', third)