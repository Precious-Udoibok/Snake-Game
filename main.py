from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
import time
from food import Food

my_screen = Screen()
my_screen.setup(600,600)
my_screen.bgcolor('black')
my_screen.title('My Snake Game.')
my_screen.tracer(0)

my_screen.listen()
#creating the snake object from the snake class
snake =  Snake()
food = Food()
my_score = Scoreboard()
#while the game is still on
is_game_on = True
while is_game_on:
    my_screen.update() #update the drawings
    time.sleep(0.1)
    #keys to control the snake movement
    my_screen.onkey(snake.up,'Up')
    my_screen.onkey(snake.down, 'Down')
    my_screen.onkey(snake.left, 'Left')
    my_screen.onkey(snake.right, 'Right')
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segement()
        #clear the zero score
        my_score.clear()
        my_score.new_score() #write the new

    #Detect collission with wall
    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor()< -280:
        is_game_on = False
        my_score.game_over()

    #Detect collision with tail
    #Removing the head by giving the second segments still the end
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            my_score.game_over()

my_screen.exitonclick()