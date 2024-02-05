# import classes Turtle, Screen from module turtle
from turtle import Turtle,Screen
# create new from turtle class

my_turtle = Turtle()
my_turtle.speed("slowest")
my_turtle.forward(250)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(100)

my_screen = Screen()
my_screen.exitonclick()