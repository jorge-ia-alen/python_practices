while True:
    try: 
        edad = int(input("Ingrese su edad: "))
        print("Tu edad es: ", edad)
        break
    except:
        print("ingresaste un valor erroneo")
    finally:
        print("La ejecución a Finalizado")#dsto se ejecuta siempre