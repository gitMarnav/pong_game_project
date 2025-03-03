from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('darkseagreen3')
screen.title("Welcome to the PONG Game ( Ver. 1.0.0 )")
screen.tracer(0)
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with both paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detect if the ball is out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        if scoreboard.l_score == 10:
            game_is_on = False
            scoreboard.game_over_l()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        if scoreboard.l_score == 10:
            game_is_on = False
            scoreboard.game_over_r()

screen.mainloop()
