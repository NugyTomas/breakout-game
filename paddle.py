from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, dimension):
        super().__init__()
        self.width = dimension.paddle_width
        self.height = dimension.paddle_height
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=self.height / 20, stretch_len=self.width / 20)
        self.penup()
        self.start_x = dimension.paddle_start_x
        self.start_y = dimension.paddle_start_y
        self.goto(self.start_x, self.start_y)

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

    def go_left(self, dimension):
        new_x = self.xcor() - int(0.2 * self.width)

        if new_x - self.width / 2 >= dimension.left_wall-self.width / 2:
            self.goto(new_x, self.ycor())

    def go_right(self, dimension):
        new_x = self.xcor() + int(0.2 * self.width)

        if new_x + self.width / 2 <= dimension.right_wall+self.width / 2:
            self.goto(new_x, self.ycor())

    def reset_position(self):
        self.goto(self.start_x, self.start_y)

    def next_level(self):
        self.width = int(self.width * 0.75)
        self.shapesize(stretch_wid=self.height / 20, stretch_len=self.width / 20)
