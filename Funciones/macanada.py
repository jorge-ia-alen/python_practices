#lista de palabras que pueden salir
import random

listaLetras = ['Mierda', 'America','pasado', 'tener', 'ser', 'el', 'la','él','ella','ellos','su','si','sí','tu','tú','dios','tenemos','random','tener','hacer','hay','que','carajo','perro','perra','gato','trabajo','trabajar']
cont,mal,bien=0,0,0
newList,validList = [],[]

#Cambia las palabras de las consola una vez que se completen las 10
#quiero que tome 10 letras random y las muestre, una al lado de la otra.

for i in range(10):
    newList.append(random.choice(listaLetras))

print(newList)

#valida que las letras sean correctas sino suma 1 al contador de errores

for i in range(10):
    validList.append(input(""))

while cont < 10:
    if newList[cont] != validList[cont]:
        mal+=1
    else:
        bien+=1
    cont+=1

print(newList)
print(validList)
print("Hiciste: {} bien y {} mal".format(bien,mal))


#
#
