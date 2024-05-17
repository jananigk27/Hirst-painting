###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import turtle
import colorgram
import random
from turtle import Turtle, Screen
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
turtle.colormode(255)
color_list = [ (202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
def dots_in_a_row():
    for _ in range(10):
        tim.pendown()
        random_color = random.choice(color_list)
        tim.dot(20, random_color)
        tim.penup()
        tim.forward(50)

def shift_row():
    dots_in_a_row()
    tim.left(90)
    tim.penup()
    tim.forward(50)
    tim.left(90)
    tim.forward(50)
    dots_in_a_row()

def original_pos():
    tim.right(90)
    tim.penup()
    tim.forward(50)
    tim.right(90)
    tim.penup()
    tim.forward(50)


for _ in range(5):
    shift_row()
    original_pos()





























screen = Screen()
screen.exitonclick()