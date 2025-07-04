import time
from turtle import Turtle,Screen
from paddles import Paddle
from ball import Ball
from score import Score

screen=Screen()
screen.tracer(0)  #animation off
screen.setup(800,600)
screen.bgcolor("black")
screen.title("PONG GAME")

l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))
ball=Ball()
score=Score()

screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")


game_is_on =True
while game_is_on:
    screen.update()
    spd=ball.speed
    time.sleep(spd)

    ball.move_ball()

    #when ball reaches up and down side , it needs to bounce back
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #when collides with right or left paddle
    if ball.distance(r_paddle)<15 and ball.xcor()>330 or ball.distance(l_paddle)<15 and ball.xcor()<-330:
        ball.bounce_x()
        ball.incr_speed()

    #when right player misses
    if ball.xcor() > 380:
        score.l_point()
        ball.restart()

    # when left player misses
    if ball.xcor() < -380:
        score.r_point()
        ball.restart()


screen.exitonclick()