from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('MY SNAKE GAME')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
