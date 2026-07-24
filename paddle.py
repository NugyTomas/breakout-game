from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, start_x, start_y, paddle_width, paddle_height):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=paddle_width, stretch_len=paddle_height)
        self.penup()
        self.goto(start_x, start_y)

    def go_left(self):
        self.goto(self.xcor() - 20, self.ycor())

    def go_right(self):
        self.goto(self.xcor() + 20, self.ycor())

