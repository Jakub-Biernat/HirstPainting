# import colorgram
import turtle as t
import random

# colors = colorgram.extract('hirst_image.jpg', 30)
# colors_rgb = []
# for color in colors:
#     rgb = color.rgb
#     colors_rgb.append(tuple(rgb))
# print(colors_rgb)


color_list = [(222, 152, 103), (233, 237, 240), (128, 172, 199), (221, 130, 149), (221, 73, 90), (243, 208, 99),
              (17, 121, 157), (118, 176, 147), (34, 120, 82), (18, 165, 204), (230, 74, 70), (142, 86, 60),
              (116, 85, 102), (162, 209, 162), (13, 169, 120), (171, 183, 219), (177, 154, 75), (213, 222, 213),
              (1, 98, 119), (54, 61, 96), (240, 177, 165), (221, 167, 185), (146, 204, 228), (24, 98, 61)]

my_turtle = t.Turtle()
my_screen = t.Screen()
my_screen.colormode(255)
def hirst_painting():
    my_turtle.penup()
    my_turtle.speed(0)
    my_turtle.setposition(-300, -300)
    starting_position = list(my_turtle.position())
    for _ in range(10):
        starting_position[1] += 50
        my_turtle.setposition(starting_position)
        for dot in range(10):
            my_turtle.dot(20, random.choice(color_list))
            my_turtle.forward(50)
    my_turtle.hideturtle()


hirst_painting()

my_screen.exitonclick()