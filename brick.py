from turtle import Turtle

class Brick(Turtle):

    def __init__(self, x, y, width, height, color, point):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.width = width
        self.height = height
        self.shapesize(stretch_wid=self.height/20, stretch_len=self.width/20)
        self.penup()
        self.goto(x,y)
        self.point = point

    # Edges
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





