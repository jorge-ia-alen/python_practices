phrase = input("Poneme alguna frase: ")
file_name = 'sos-' + phrase + '.txt'
f = open(file_name, 'w')
f.write(phrase + 'shit')
f.close()