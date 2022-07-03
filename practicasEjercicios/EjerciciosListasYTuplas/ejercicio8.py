# palabra = input("Dame una palabra para saber si es un palindromo: ")
# palabraDoblada = palabra[::-1]
# if palabra == palabraDoblada:
# 	print("{} and {} es un palindromo porque se lee igual al revez".format(palabra,palabraDoblada))
# else:
# 	print("No es un palindromo")

#La idea era hacerlo una lista XD


word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")