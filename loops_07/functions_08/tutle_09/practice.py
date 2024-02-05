import turtle
from turtle import Turtle ,Screen
colors=["red","blue","yellow","orange","brown","green"]
my_turtle=Turtle()
my_turtle.speed(10)
my_turtle.pen()
turtle.bgcolor("black")
for i in range(360):
    my_turtle.pencolor(colors[i%6])
    my_turtle.width(i/100+1)
    my_turtle.forward(i)
    my_turtle.left(59)


my_screen=Screen()
my_screen.exitonclick()