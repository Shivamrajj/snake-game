from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scorecard import Scoreboard

screen = Screen()
screen.setup(width=700, height=600)
screen.bgcolor("brown")
screen.title("MY SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Up', fun=snake.up)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.food_pos()
        score.update_score()
        snake.update_snake_length()

    #  CHECK SNAKE COLLISION WITH WALL

    if (snake.head.xcor() >= 350 or snake.head.xcor() <= -350 or snake.head.ycor() >= 300
            or snake.head.ycor() <= -300):
        is_game_on = False
        screen.reset()
        score.game_over()

    if snake.check_collision() == False:
        is_game_on = False
        screen.reset()
        score.game_over()



screen.exitonclick()