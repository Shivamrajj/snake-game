import random
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('blue')
        self.shapesize(stretch_len=0.6 , stretch_wid=0.6)
        self.penup()
        self.speed("fastest")
        self.food_pos()


    def food_pos(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

