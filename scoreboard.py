from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier',24,'normal')

#class to keep record of the scores.
class Scoreboard(Turtle):
    #inheriting the turtle class
    def __init__(self):
        #inheriting the functions from the turtle class
        super().__init__()
        self.x = 0
        self.penup()
        self.color('White')
        self.goto(0,260) #set the turtle to the top of the screen
        self.write(arg=f'Score = {self.x}',move=False,align= ALIGNMENT,font=FONT)
        self.color('White')
        self.hideturtle()
    def new_score(self):
        '''increment the score by 1 and display the new score.'''
        self.x+=1
        self.write(arg=f'Score = {self.x}',move=False,align=ALIGNMENT,font=FONT)

    def game_over(self):
        '''turtle goes to the center of the screen and write Game OVER'''
        self.goto(0,0)
        self.write(arg='GAME OVER',move=False,align=ALIGNMENT,font=FONT)
