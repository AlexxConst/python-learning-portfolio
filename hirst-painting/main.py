import turtle

import turtle as t
import random

t.colormode(255)

"""
10 x 10
each dots 20size and space 50
"""
# setup turtle
tim = t.Turtle()
tim.penup()
tim.speed('fastest')
tim.hideturtle()

tim.setheading(230)
tim.forward(350)
tim.setheading(0)

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5),
              (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12),
              (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229),
              (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198),
              (65, 231, 239), (217, 88, 51)]

num_dots = 100

for dot_count in range(1, num_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.mainloop()
turtle.exitonclick()
