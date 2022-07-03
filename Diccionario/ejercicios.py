'''diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Tegucigalpa","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = input("Ingresa un pais: ")

if pais.title() in diccionario:
    print(diccionario[pais.title()])
else:
    print("El pais no se encuentra en el diccionario")'''


diccionario = {

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}

jugador = int(input("Ingresa un nro para ver el nombre de un Jugador: "))

if jugador in diccionario:
    print("El numero {} es {}".format(jugador, diccionario[jugador]))
else:
    print("No se encuentra un jugador con ese numero")
