from turtle import Turtle

class Ball(Turtle):

    def __init__(self, start_x, start_y, ball_radius):
        super().__init__()
        self.radius = ball_radius
        self.color("white")
        self.shape("circle")
        self.penup()
        self.start_x = start_x
        self.start_y = start_y
        self.goto(start_x,start_y)
        self.x_move = -4
        self.y_move = -7
        self.paddle_hits = 0

    @property
    def left_edge(self):
        return self.xcor() - self.radius
    @property
    def right_edge(self):
        return self.xcor() + self.radius
    @property
    def top_edge(self):
        return self.ycor() + self.radius
    @property
    def bottom_edge(self):
        return self.ycor() - self.radius

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def paddle_bounce(self, relative_hit):
        self.y_move *= -1

        if relative_hit <= -0.45:
            self.x_move = -abs(1.2 * self.x_move)
        elif relative_hit <= -0.1:
            self.x_move = -abs(0.9 * self.x_move)
        elif relative_hit <= 0.1:
            self.x_move *= -0.8
        elif relative_hit <= 0.45:
            self.x_move = abs(0.9 * self.x_move)
        else:
            self.x_move = abs(1.2 * self.x_move)

    def x_bounce(self):
        self.x_move *= -1

    def y_bounce(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(self.start_x, self.start_y)
