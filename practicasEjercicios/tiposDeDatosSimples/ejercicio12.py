pan,descuento,barras=3.49,0.6,int(input("Cuantas barras pan pasadas tienes?: "))
precioFinal=(pan*(1-descuento))*barras
print("Lo que se cobrará por los panes no frescos es: {} Euros".format(round(precioFinal,2)))