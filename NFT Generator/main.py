import turtle
import random

angles = [0, 90, 180, 270]


def rn_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    gen.pencolor(r, g, b)


if __name__ == "__main__":
    gen = turtle.Turtle()
    gen.pensize(8)
    iteration = int(input("Enter a number for iteration: "))
    screen = turtle.Screen()
    screen.colormode(255)
    for x in range(iteration):
        gen.forward(random.randint(0, 180))
        gen.setheading(random.choice(angles))
        rn_color()
    turtle.exitonclick()
