from turtle import Screen
from ball import Ball
from gamedimension import GameDimension
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.title("Breakout")

monitor_width = screen.cv._rootwindow.winfo_screenwidth()
monitor_height = screen.cv._rootwindow.winfo_screenheight()

dimension = GameDimension(monitor_width, monitor_height)

screen.setup(width=dimension.window_width, height=dimension.window_height)
screen.cv._rootwindow.resizable(False, False)
screen.tracer(0)

paddle = Paddle(dimension.paddle_start_x, dimension.paddle_start_y, dimension.paddle_width, dimension.paddle_height)
ball = Ball(dimension.ball_start_x, dimension.ball_start_y, dimension.ball_radius)

screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

def game_loop():
    screen.update()
    ball.move()

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

    screen.ontimer(game_loop, 10)

game_loop()
screen.mainloop()