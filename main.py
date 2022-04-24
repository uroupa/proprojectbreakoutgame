from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddle import Paddle
from paddle import Obstacles
from ball import Ball
import time


def check_win(n_list):
    return all(not n.isvisible() for n in n_list)


screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

scoreboard = Scoreboard()
paddle = Paddle((0, -350))
ball = Ball()

positions = [(225, 350), (150, 350), (75, 350), (0, 350), (-75, 350), (-150, 350), (-225, 350),
             (225, 375), (150, 375), (75, 375), (0, 375), (-75, 375), (-150, 375), (-225, 375)]

obstacles = [Obstacles(position=pos) for pos in positions]

screen.listen()
screen.onkey(key="Left", fun=paddle.move_left)
screen.onkey(key="Right", fun=paddle.move_right)


game_is_on = True

while game_is_on:
    screen.update()
    ball.move_ball()
    for obstacle in obstacles:
        obstacle.move_down()


#####   BALL PHYSICS   #####
    if ball.ycor() > 380:
        ball.bounce_y()
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()
    if ball.distance(paddle) < 65 and ball.ycor() < -320:
        ball.bounce_y()
    if ball.ycor() < -400:
        ball.reset_position()
        scoreboard.negative_point()

#####   OBSTACLE AND BALL PHYSICS   #####
    for obstacle in obstacles:
        if ball.distance(obstacle) < 40 and obstacle.isvisible():
            ball.bounce_y()
            obstacle.hideturtle()
            scoreboard.point()


        ###### END GAME CONDITIONS ######
        if obstacle.ycor() < -360:
            scoreboard.game_over()
            game_is_on = False

    if check_win(obstacles):
        scoreboard.game_won()
        game_is_on = False

    if scoreboard.score == -50:
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()