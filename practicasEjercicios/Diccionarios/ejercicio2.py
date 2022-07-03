nombre,edad,direccion,telefono = input('Cual es tu nombre?: '), int(input('Cual es tu edad?: ')), input('Cual es tu direccion?: '), input('Cual es tu nro de telefono?: ')
datos = {"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono}
print('{} tiene {} anhos, vive en {} y su nro de telefono es {}'.format(datos["nombre"], datos["edad"], datos["direccion"],datos["telefono"]))