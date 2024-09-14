from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.35, stretch_wid=0.35)
        self.color("blue")
        self.pu()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-210, 210)        # 250 FOR SCREEN @600X600
        random_y = random.randint(-210, 210)        # 250 FOR SCREEN @600X600
        self.goto(random_x, random_y)
