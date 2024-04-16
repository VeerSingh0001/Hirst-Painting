import turtle
from random import choice

tim = turtle.Turtle(visible=False)
screen = turtle.Screen()
turtle.colormode(255)
color_list = [(139, 80, 53), (185, 163, 125), (138, 166, 176), (60, 111, 134), (17, 42, 73), (139, 62, 88), (162, 153, 44), (66, 119, 101), (147, 182, 171), (215, 210, 107), (76, 34, 29), (69, 151, 163), (115, 39, 32), (96, 145, 119), (177, 148, 162), (74, 30, 35), (168, 99, 127), (33, 56, 105), (104, 123, 165),
              (107, 40, 49), (175, 106, 90), (209, 181, 194), (21, 96, 86), (169, 202, 196), (9, 97, 112), (220, 178, 172)]

# turtle.delay(0)
# tim.speed(0)

x = -250  # Starting x-axis
y = -250  # Starting y-axis

for _ in range(10):
    tim.penup()
    tim.sety(y)
    for _ in range(10):
        random_col = choice(color_list)
        tim.setx(x)
        tim.dot(20, random_col)
        tim.penup()
        x += 50

    x = -250
    y += 50
screen.exitonclick()
