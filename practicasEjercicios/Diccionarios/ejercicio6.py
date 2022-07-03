datos = {"nombre": '', "edad": '', "sexo": '', "telefono":'', "correo electronico":''}
dato_key, dato_value = list(datos.keys()), list(datos.values())
for i in range(5):
	a = input('Cual es tu {}?: '.format(dato_key[i]))
	datos[i] = a
	print(datos[i])

#solo para ver el diccionario, no parte del codigo
print(datos)


# en realidad este tuvo que ser el codigo, no lo entendi tan bien, o el problema no lo explicaba bien
persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"