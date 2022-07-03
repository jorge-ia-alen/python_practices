#libraries
import turtle
import random

#default settings

s = turtle.Screen()
t1 = turtle.Turtle()
t2 = turtle.Turtle()

listaNum = [1,2,3,4,5,6]

t1.hideturtle()
t2.hideturtle()

t1.shape("turtle")
t2.shape("turtle")

t1.pencolor("white")
t1.sety(100)

#Functions:
def CreacionMetas():
    t1.color("white","red")
    t1.forward(300)
    t1.color("red","red")
    t1.circle(30)
    t1.left(180)
    t1.color("white","red")
    t1.forward(500)
    t1.right(180)

    t2.color("white","blue")
    t2.forward(300)
    t2.color("blue","blue")
    t2.circle(30)
    t2.left(180)
    t2.color("white","blue")
    t2.forward(500)
    t2.right(180)

def pintarTortugas():
    t1.showturtle()
    t2.showturtle()

    t1.sety(120)
    t2.sety(20)

    t1.color("red","red")
    t2.color("blue","blue")

def Competicion():
    n,n2,nmas,cont=0,0,0,0
    while cont < 11:
        if cont % 2 != 0:
            nmas = random.choice(listaNum)*10
            n+=nmas
            if n < 480:
                t1.forward(n)
                cont+=1

        elif cont % 2 == 0:
            nmas = random.choice(listaNum)*10
            n2+=nmas
            if n2 < 480:
                t2.forward(n2)
                cont+=1
        
        else:
            print("El contador: {}".format(cont))
            break

        




#default line
CreacionMetas()
pintarTortugas()
Competicion()
turtle.done()


""" if cont == 0:
            nmas = random.choice(listaNum)
            n+=nmas
            if n < 480:
                t1.forward(n)
                cont+=1
            else:
                cont = 2
                break
            
        elif cont == 1:
            nmas = random.choice(listaNum)
            n2+=nmas
            if n2 < 480:
                t2.forward(n2)
                cont-=1
            else:
                cont = 2
                break

        elif cont == 2:
            print("No sé que carajos pasa")
            break """