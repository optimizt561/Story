from turtle import Turtle
from snake import Snake
from random import randint

class Food(Turtle):           # illustrating inheritance

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('coral')
        self.speed('fastest')
        random_x = randint(-200, 200)
        random_y = randint(-200, 200)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = randint(-200, 200)
        random_y = randint(-200, 200)
        self.goto(random_x, random_y)