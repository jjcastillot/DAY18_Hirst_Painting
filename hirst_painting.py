# Colorgram importing with image
import colorgram
from turtle import Turtle, Screen, colormode
import random
colormode(255)
colors = colorgram.extract('Hirst.jpg',12)

# Create rgb colors list
rgb_colors = []
for color in colors:
    new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
    rgb_colors.append(new_color)

# Start to paint
dots = 10

artist = Turtle()
artist.pensize(10)
artist.speed('fastest')
artist.penup()
artist.setheading(210)
artist.forward(400)
artist.setheading(0)

for i in range(dots):
    for j in range(dots):
        artist.dot(20,random.choice(rgb_colors))
        artist.penup()
        artist.forward(artist.pensize()*4)
    artist.setheading(90)
    artist.forward(artist.pensize()*4)
    artist.setheading(180)
    artist.forward(artist.pensize()*4*dots)
    artist.setheading(0)

screen = Screen() 
screen.exitonclick()

