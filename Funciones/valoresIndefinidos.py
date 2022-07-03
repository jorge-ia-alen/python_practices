#def argumento(*num): Así es una tupla
def argumento(*num):
    return type(num)

print(argumento(10, 20, 30, 40, 50))