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
        self.start_x_speed = -4
        self.start_y_speed = -7

        self.x_move = self.start_x_speed
        self.y_move = self.start_y_speed

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

        if relative_hit <= -0.7:
            self.x_move = -abs(1.35 * self.x_move)
        elif relative_hit <= -0.4:
            self.x_move = -abs(1.15 * self.x_move)
        elif relative_hit <= -0.15:
            self.x_move = -abs(0.9 * self.x_move)
        elif relative_hit <= 0.15:
            self.x_move *= -0.4
        elif relative_hit <= 0.4:
            self.x_move = abs(0.9 * self.x_move)
        elif relative_hit <= 0.7:
            self.x_move = abs(1.15 * self.x_move)
        else:
            self.x_move = abs(1.35 * self.x_move)

        if abs(self.y_move) < 4:
            self.y_move = 4 if self.y_move > 0 else -4

        if abs(self.x_move) < 2:
            self.x_move = 2 if self.x_move > 0 else -2

    def x_bounce(self):
        self.x_move *= -1

    def y_bounce(self):
        self.y_move *= -1

    def reset(self):
        self.goto(self.start_x, self.start_y)

        self.x_move = self.start_x_speed
        self.y_move = self.start_y_speed

        self.paddle_hits = 0