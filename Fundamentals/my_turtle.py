import turtle
import math

def draw_circle(r):
    for i in range(360):
        turtle.lt(1)
        turtle.fd(math.pi * r / 180)

for i in range(6):
    draw_circle(100)
    turtle.lt(60)

turtle.pu()
turtle.fd(100)
turtle.lt(90)
turtle.pd()
draw_circle(100)

turtle.done()
