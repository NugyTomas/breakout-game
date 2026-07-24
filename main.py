from turtle import Screen
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

screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

def game_loop():

    screen.update()

    screen.ontimer(game_loop, 10)

game_loop()
screen.mainloop()