from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        #Creating the food for the snake
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        self.color('blue')
        self.refresh()

    def refresh(self):
        '''THE TURTLE(FOOD) GOES TO A RANDOM POPSITION.'''
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)