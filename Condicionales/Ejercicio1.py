vocal = input("Dame una Vocal: ")

if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
    print("Es la vocal: ", vocal)
else:
    print("A CASO '{}' te parece una vocal TAVY GALACTICO?".format(vocal))

#otra manera
if vocal in "aeiou":
    print("Es una vocal")
else: 
    print("No es una vocal")