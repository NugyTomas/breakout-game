from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, start_x, start_y, paddle_width, paddle_height):
        super().__init__()
        self.width = paddle_width
        self.height = paddle_height
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=self.height/20, stretch_len=self.width/20)
        self.penup()
        self.start_x = start_x
        self.start_y = start_y
        self.goto(start_x, start_y)

    @property
    def left_edge(self):
        return self.xcor() - self.width / 2

    @property
    def right_edge(self):
        return self.xcor() + self.width / 2

    @property
    def top_edge(self):
        return self.ycor() + self.height / 2

    @property
    def bottom_edge(self):
        return self.ycor() - self.height / 2

    def go_left(self):
        self.goto(self.xcor() - int(0.2 * self.width), self.ycor())

    def go_right(self):
        self.goto(self.xcor() + int(0.2 * self.width), self.ycor())

    def reset_position(self):
        self.goto(self.start_x, self.start_y)
