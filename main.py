# Create the screen
# Create and move a paddle
# Create another paddle
# Create the ball and make it move
# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when paddle misses
# Scoreboard

from turtle import Turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.tracer(0) # screen sie nie odswieza, ale nie ma animacji> manualnie odswiezyc potem


r_paddle = Paddle((350, 0)) # tuple here is 2 args like a 1arg
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen(ball.move_speed)
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_flag = True
while game_flag:
    time.sleep(ball.move_speed) # give a pause between frames, if ball is moving -slower
    screen.update()
    ball.move()

    # detect collision with a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # #detect collision with r_paddle
    # if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
    #     ball.bounce_x()

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    ## left and right in separate because of scoreboard to one side
    # detect if right paddle missed the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    #detect if left paddle missed the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
