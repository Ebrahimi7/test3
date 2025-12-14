import turtle
import random

###################################################3

t = turtle.Turtle()
# def star():
#     t.speed(0)
#     colors = ["red", "blue", "green", "yellow", "purple", "orange"]

#     for i in range(50):
#         t.color(colors[i % 6])
#         t.forward(100)
#         t.right(144)
#         t.forward(50)
#         t.left(80)
    
# star()

# def flower():
#     t.speed(0)
#     t.color("#ab1265")

#     for i in range(10000):
#         t.circle(70)
#         t.right(-1)

# flower()

# def house():
#     t.speed(3)

#     for _ in range(4):
#         t.forward(100)
#         t.left(90)

#     t.left(45)
#     t.forward(70)
#     t.left(90)
#     t.forward(70)

# house()


# def rainbow_dots():
#     t.speed(0)
#     t.penup()

#     colors = ["red", "blue", "green", "yellow", "purple", "orange",'#256341',"#DE8693"]

#     for i in range(100):
#         t.goto(random.randint(-200,200), random.randint(-200,200))
#         t.dot(random.randint(10,40), random.choice(colors))

# rainbow_dots()



# def spiral():
#     t.speed(0)
#     colors = ["red", "green", "blue", "purple", "orange"]

#     for i in range(250):
#         t.color(colors[i % 5])
#         t.forward(i)
#         t.left(59)

# spiral()


# def rotating_circles():
#     t.speed(0)

#     colors = ["red", "blue", "green", "purple", "yellow"]

#     for i in range(72):
#         t.color(colors[i % 5])
#         t.circle(100)
#         t.left(5)

# rotating_circles()

# def nested_stars():
#     t.speed(0)

#     for size in range(20, 500, 10):
#         t.color("purple")
#         for _ in range(5):
#             t.forward(size)
#             t.right(144)
#         t.right(10)

# nested_stars()

# def snowflake():
#     t.speed(0)
#     t.color("blue")

#     for i in range(80):
#         for j in range(3):
#             t.forward(100)
#             t.left(120)
#         t.left(45)
# snowflake()


# def rotating_squares():
#     t.speed(0)

#     colors = ["red", "orange", "yellow", "green", "blue"]

#     for i in range(70):
#         t.color(colors[i % 5])
#         for _ in range(4):
#             t.forward(150)
#             t.left(90)
#         t.left(7)
# rotating_squares()

import math

def rose():
    t.speed(0)
    t.color("magenta")

    for angle in range(360 * 4):
        r = 150 * math.sin(10 * math.radians(angle))
        x = r * math.cos(math.radians(angle))
        y = r * math.sin(math.radians(angle))
        t.goto(x, y)


rose()
