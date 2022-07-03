phrase, word,cont = input("Dame una frase: "), input("Dame una letra: "),0
for i in phrase:
	if i == word:
		cont += 1
print("La letra '{}' aparece {} en la frase".format(word,cont))