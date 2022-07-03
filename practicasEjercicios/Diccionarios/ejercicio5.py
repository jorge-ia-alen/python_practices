asignaturas,suma={'Matemáticas': 6, 'Física': 4, 'Química': 5},0
list_keys,list_values = list(asignaturas.keys()), list(asignaturas.values())
for i in range(len(asignaturas)):
	print('la asignatura {} tiene {} creditos'.format(list_keys[i], list_values[i]))
	suma += list_values[i]
print('el nro de creditos del curso es: {}'.format(suma))

# curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
# total_creditos = 0
# for asignatura, creditos in curso.items():
#     print(asignatura, 'tiene', creditos, 'créditos')
#     total_creditos += creditos
# print('Número total de créditos del curso: ', total_creditos)