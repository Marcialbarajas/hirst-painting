# import colorgram
import turtle as t
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 32)

# for color in colors:
#    r = color.rgb.r
#   g= color.rgb.g
#    b = color.rgb.b
#    new_color = (r,g,b)
#    rgb_colors.append(new_color)

# print (rgb_colors)
turtle_module = t.colormode(255)

timmy = t.Turtle()

color_list = [(249, 246, 240), (239, 245, 250), (250, 242, 247), (243, 251, 246), (139, 164, 184), (27, 114, 171),
              (202, 141, 167), (237, 213, 67), (219, 157, 89), (22, 136, 66), (139, 21, 37), (124, 72, 94),
              (185, 176, 26), (70, 30, 37), (182, 73, 41), (225, 170, 197), (52, 36, 34), (232, 83, 40), (39, 174, 99),
              (108, 190, 136), (9, 107, 64), (29, 169, 185), (181, 95, 112), (38, 37, 43), (239, 216, 8),
              (188, 184, 210), (158, 207, 215), (152, 214, 174), (240, 169, 154), (105, 41, 39), (116, 120, 162),
              (71, 53, 93)]
timmy.speed("fastest")
timmy.shape("turtle")
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.pendown()
number_of_dots=100

for dot_count in range(1, number_of_dots):
    timmy.pendown()
    timmy.dot(20, random.choice(color_list))
    timmy.penup()
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.fd(500)
        timmy.setheading(0)


screen = t.Screen()
screen.exitonclick()

