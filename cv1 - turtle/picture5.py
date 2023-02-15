import turtle
from turtle import *

f = 50

for i in range(2,7):
    turtle.forward(f)
    turtle.left(90)
    turtle.forward(50)
    turtle.setheading(turtle.towards(0,0))
    f = turtle.distance(0,0)

    turtle.forward(f)
    turtle.left(180)

turtle.forward(f)
turtle.left(90)
turtle.forward(50)

done()