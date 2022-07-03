compras = {}
continuar = True
while continuar:
    clave = input('¿Que elemento comprara? ')
    valor = float(input(clave + ' cuesta : '))
    compras[clave] = valor
    print(compras)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"

articulos = len(compras)
key_list, value_list,suma = list(compras.keys()), list(compras.values()), 0

for i in range(articulos):
    print('{} cuesta {}'.format(key_list[i], value_list[i]))
    suma += value_list[i]
print('El coste total es {}'.format(suma))