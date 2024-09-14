from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

# Necessary package installation #######################################################################################
import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


########################################################################################################################
screen = Screen()

size = 0.5  # default width of the turtle.To customize assign size to be the size of the snake while making its object

snake = Snake(size)
food = Food()

snake.create_snake()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)
    if snake.collision_with_tail():
        snake.reset()
        scoreboard.reset_score()

    # Detect collision with food
    if snake.head.distance(food) < 10:
        scoreboard.update()
        snake.extend()
        food.refresh()

    # Detect collision with wall
    if snake.head.xcor() > 225 or snake.head.xcor() < -225 or snake.head.ycor() > 225 or snake.head.ycor() < -225:
        # +-260 FOR SCREEN @600X600
        snake.reset()
        scoreboard.reset_score()

screen.exitonclick()
