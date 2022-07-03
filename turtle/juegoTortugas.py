from tkinter.tix import ListNoteBook
import turtle
import random

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

def pintarMetas():
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

#movimiento de las tortugas
def movimientoTortugas():
    cont=0
    n,nmas,nmas2,n2,m,m2=0,0,0,0,0,0
    #desplazamiento:
    while cont < 10:
        if cont % 2 != 0:
            nmas = random.choice(listaNum)*3
            n+=nmas
            cont+=1
            if cont == 9:
                n = n*3
                if n > 480:
                    m = n - 480
                    n-=m
                elif n > n2 and n < 480:
                    m = 480 - n
                    n+=m
                else:
                    break
            else:
                print("El fordware de n es {}".format(n))

            
        elif cont %2 == 0:
            nmas2 = random.choice(listaNum)*3
            n2+=nmas2
            cont+=1
            if cont == 9:
                n2 = n2*3
                if n2 > 480:
                    m = n2 - 480
                    n2-=m
                elif n2 > n and n2 < 480:
                    m = 480 - n2
                    n2+=m
                else:
                    break

            else:
                print("El fordware de n2 es {}".format(n2))
            
        t1.forward(n)
        t2.forward(n2)




pintarMetas()
pintarTortugas()
movimientoTortugas()
turtle.done()