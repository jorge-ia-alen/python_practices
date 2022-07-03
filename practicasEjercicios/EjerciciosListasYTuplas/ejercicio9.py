vocals, word = ["a","e","i","o","u"],input("Dame una palabra: ")
list(word)
for vocal in vocals:
	cont = 0
	for letter in word: 
		if letter == vocal:
			cont+= 1
	print("La vocal {} esta {}".format(vocal, str(cont)))
#Tuve que ver porque no entendia