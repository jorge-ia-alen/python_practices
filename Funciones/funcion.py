""" def fib(n):
    a,b = 0,1
    while a < n:
        print(a, end=' ')
        a,b = b, a+b
    print() """

#fib(2000)
#f = fib
#print(f(0))

""" def fib2(n):
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a,b = b, a+b
    return result

f100 = fib2(100)
f100

print(f100) """



""" from argparse import REMAINDER
from math import remainder


def ask_ok(prompt, retries=4, remider='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n', 'no', 'nop','nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user response B1tch3$')
        print(remider) """


""" def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3)) """

""" def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000000, action='VOOOOOOOM')
parrot(action='VOOOOM', voltage=1000000)
parrot('a million','bereft of life', 'jump')
parrot('a thousand', state='pushing up the daisies') """


#Funciones curso:(funciones propias)
""" num = "70"
lista=[12,60,70, 1, -2]

print(type(num))
print(type(int(num)))
print(type(lista))
print(max(lista))
print(min(lista)) """

#funciones
def saludo():
    print("Hola Walter Coto")

saludo()

def tabla7():
    for i in range(11):
        print("7 x {} = {}".format(i, i*7))

tabla7()