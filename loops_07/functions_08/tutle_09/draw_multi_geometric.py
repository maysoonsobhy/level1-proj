import random
from turtle import Turtle ,Screen

my_turtle = Turtle()
my_turtle.shape(100)
shapes_list = ["tringle","square","grey","","","","Octagon","Decagon"]
for i in range(15):
  my_turtle.left(15)
  chosen_color =random.choice(colors_list)
  my_turtle.color(chosen_color)
  my_turtle.circle(100)



my_screen = Screen()
my_screen.exitonclick()