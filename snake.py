from turtle import Turtle


MOVEMENT = 20
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
UP =90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        #ATTRIBUTES OF THE SNAKE CLASS
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    #function to create the snake
    def create_snake(self):
        for squares in STARTING_POSITION:
            self.add_segment(squares)

    #function to add segements to the snake
    def add_segment(self,squares):
        square = Turtle(shape='square')
        square.color('white')
        square.penup()
        square.setpos(squares)
        self.snake.append(square)

    #function to extend the length of the snake
    def extend_segement(self):
        self.add_segment(self.snake[-1].position())

    #function to move the snake.
    #moving the snake backwards, the last position comes to the second
    #the second comes to the first..
    def move(self):
        #moving the sanke in the step of -1.
        for snake_no in range(len(self.snake) - 1, 0, -1):

            #create a new x and y coordinate
            new_x = self.snake[snake_no - 1].xcor()
            new_y = self.snake[snake_no - 1].ycor()
            self.snake[snake_no].setpos(new_x, new_y)
            # after the last two snake have move.. you move the first segment or snake forward
        self.head.forward(MOVEMENT)

    #functions to move the snake up,down left and right
    #making sure that the snake does not go the opposite direction.
    #if its up, it's can't go down.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


