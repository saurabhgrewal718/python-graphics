import turtle
from itertools import cycle

colors=cycle(['red','orange','yellow','green','blue','purple'])

def draw_circle(size,angle,shift):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+2,angle+1,shift+1)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(5)
draw_circle(20,0,1)
