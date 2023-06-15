from turtle import Turtle,Screen
import colorgram
import random
timmy = Turtle()

colors = colorgram.extract('image.jpg',30)
color_list = [ (232, 251, 242), (198, 13, 32), (250, 237, 19), (39, 76, 189), (39, 217, 68), (238, 227, 5), (229, 159, 47), (28, 40, 156), (214, 75, 13), (242, 246, 252), (16, 154, 16), (198, 15, 11), (243, 34, 165), (68, 10, 30), (228, 18, 120), (60, 15, 8), (223, 141, 209), (11, 97, 62), (221, 161, 9), (50, 212, 231), (18, 20, 47), (11, 227, 239), (238, 156, 217), (84, 74, 211), (78, 210, 163), (82, 234, 200), (61, 233, 241), (5, 68, 42)]
screen = Screen()
screen.colormode(255)
timmy.penup()
timmy.goto(-250,-250)
normal_y = timmy.ycor()
i = 0
def go_forward():
    for _ in range(10):
        timmy.dot(20,random.choice(color_list))
        timmy.forward(50)

def paint():
    for _ in range(10):
        global i
        i+= 50
        go_forward()
        timmy.goto(-250,normal_y+i)

paint()
screen.exitonclick()

