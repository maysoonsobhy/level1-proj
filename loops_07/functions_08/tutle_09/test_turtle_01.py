# program to show how to use turtle
# import classes turtle ,screen from module turtle
from turtle import Turtle , Screen


# create  new object from turtle class
my_turtle = Turtle()
for i in range(4):
  my_turtle.forward(100)
  my_turtle.left(90)
#my_turtle.forward(300)
#my_turtle.left(90)
#my_turtle.forward(100)

#my_turtle.left(90)
#my_turtle.forward(300)

#my_turtle.left(90)
#my_turtle.forward(100)




# create new object from screen class
my_screen = Screen()
my_screen.exitonclick()
