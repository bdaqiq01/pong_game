
from turtle import Shape, Screen, Turtle, register_shape, Screen

from paddle import Paddle
from ball import Ball
import time
from points import ScoreBoard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

#set up a line
line = Turtle()
line.color("white")
line.penup()
line.setheading(90)
line.goto(0, -285)
line.width(width=5)
line.hideturtle()

#middle line
for _ in range(20):
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(20)

left_paddle = Paddle(xpos=-380)
right_paddle = Paddle(xpos=370)
left_Score = ScoreBoard(x_pos=-60)
right_Score = ScoreBoard(x_pos= 60)

screen.listen()
screen.onkey(left_paddle.up, "a")
screen.onkey(left_paddle.down, "z")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

myBall = Ball()
Game_is_on = True
while Game_is_on:
    time.sleep(0.05)
    screen.update()
    myBall.move_ball()
    left_Score.show_score()
    right_Score.show_score()
    if abs(myBall.ycor()) > 280:
        myBall.bounce_wall()
    #bounce off of the right paddle
    if myBall.distance(right_paddle) < 50 and myBall.xcor() > 355: #it seems like it goes through this loop multiple times
        right_Score.clear()
        myBall.bounce_paddle()
        right_Score.add_score()

    if myBall.distance(left_paddle) < 50 and myBall.xcor() < -365:
        myBall.bounce_paddle()
        left_Score.clear()
        left_Score.add_score()
    if abs(myBall.xcor()) > 390:
        right_Score.game_over()
        Game_is_on = False


screen.exitonclick()