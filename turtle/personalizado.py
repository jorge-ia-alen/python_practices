import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor("red")
s.title("Proyecto 1")

#Ancho, largo, borde
t.shapesize(10, 5, 1)
t.shapesize(5,10,1)
t.shapesize(3,3,3)

t.fillcolor("orange")
t.pencolor("white")#Borde

t.forward(100)

t.color("green","blue")#Color del printado, color de la tortuga
t.right(90)
t.forward(100)

t.pensize(5)#grosor de la linea
t.forward(100)

turtle.done()