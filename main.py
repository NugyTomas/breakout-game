from turtle import Screen, Turtle
import time
from ball import Ball
from gamedimension import GameDimension
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("Breakout")

monitor_width = screen.cv._rootwindow.winfo_screenwidth()
monitor_height = screen.cv._rootwindow.winfo_screenheight()

dimension = GameDimension(monitor_width, monitor_height)

screen.setup(width=dimension.window_width, height=dimension.window_height)
screen.cv._rootwindow.resizable(False, False)
screen.tracer(0)

scoreboard = Scoreboard(dimension.scoreboard_y, dimension.scoreboard_font_size, dimension.left_x, dimension.right_x, dimension.high_score_y)
paddle = Paddle(dimension.paddle_start_x, dimension.paddle_start_y, dimension.paddle_width, dimension.paddle_height)
ball = Ball(dimension.ball_start_x, dimension.ball_start_y, dimension.ball_radius)

screen.listen()

message = Turtle()
message.hideturtle()
message.penup()
message.color("white")
message.goto(0, 0)

def countdown():
    for number in (3, 2, 1):
        message.clear()
        message.write(str(number),align="center",font=("Courier", int(dimension.scoreboard_font_size * 3), "bold"))
        screen.update()
        time.sleep(1)

    message.clear()

def reset_round():
    scoreboard.update_scoreboard()
    ball.reset_position()
    paddle.reset_position()
    countdown()

def game_loop():
    screen.update()
    ball.move()

    for key in ["a", "A", "Left"]:
        screen.onkeypress(paddle.go_left, key)

    for key in ["d", "D", "Right"]:
        screen.onkeypress(paddle.go_right, key)

    # Detect collision with paddle
    horizontal_hit = (
        ball.right_edge >= paddle.left_edge and ball.left_edge <= paddle.right_edge
    )

    vertical_hit = (
        ball.bottom_edge <= paddle.top_edge and ball.top_edge >= paddle.bottom_edge
    )

    if ball.y_move < 0 and horizontal_hit and vertical_hit:
        offset = ball.xcor() - paddle.xcor()
        relative_hit = offset / (paddle.width/2)
        ball.paddle_bounce(relative_hit)


    #Detect collision with walls
    if ball.left_edge <= dimension.left_wall:
        ball.x_wall_bounce()

    if ball.right_edge >= dimension.right_wall:
        ball.x_wall_bounce()

    if ball.top_edge >= dimension.top_wall:
        ball.y_wall_bounce()

    # Detect collision with bottom wall
    if ball.top_edge <= dimension.bottom_wall:
        scoreboard.lives -= 1

        if scoreboard.lives > 0:
            reset_round()
        else:
            message.write("GAME OVER ",align="center",font=("Courier", int(dimension.scoreboard_font_size * 4), "bold"))
            return

    screen.ontimer(game_loop, 10)

countdown()
game_loop()
screen.mainloop()