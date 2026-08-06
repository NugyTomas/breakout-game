from turtle import Turtle

MIN_X_SPEED = 2
MIN_Y_SPEED = 4

HARD_HIT_MULTIPLIER = 1.35
MEDIUM_HIT_MULTIPLIER = 1.15
SOFT_HIT_MULTIPLIER = 0.9
CENTER_HIT_MULTIPLIER = 0.4

class Ball(Turtle):

    def __init__(self, dimension):
        super().__init__()
        self.radius = dimension.ball_radius
        self.color("white")
        self.shape("circle")
        self.penup()
        self.start_x = dimension.ball_start_x
        self.start_y = dimension.ball_start_y
        self.goto(self.start_x,self.start_y)
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
            self.x_move = -abs(HARD_HIT_MULTIPLIER * self.x_move)
        elif relative_hit <= -0.4:
            self.x_move = -abs(MEDIUM_HIT_MULTIPLIER * self.x_move)
        elif relative_hit <= -0.15:
            self.x_move = -abs(SOFT_HIT_MULTIPLIER * self.x_move)
        elif relative_hit <= 0.15:
            self.x_move *= -CENTER_HIT_MULTIPLIER
        elif relative_hit <= 0.4:
            self.x_move = abs(SOFT_HIT_MULTIPLIER * self.x_move)
        elif relative_hit <= 0.7:
            self.x_move = abs(MEDIUM_HIT_MULTIPLIER * self.x_move)
        else:
            self.x_move = abs(HARD_HIT_MULTIPLIER * self.x_move)

        if abs(self.x_move) < MIN_X_SPEED:
            self.x_move = MIN_X_SPEED if self.x_move > 0 else -MIN_X_SPEED

        if abs(self.y_move) < MIN_Y_SPEED:
            self.y_move = MIN_Y_SPEED if self.y_move > 0 else -MIN_Y_SPEED

    def x_bounce(self):
        self.x_move *= -1

    def y_bounce(self):
        self.y_move *= -1

    def reset(self):
        self.goto(self.start_x, self.start_y)

        self.x_move = self.start_x_speed
        self.y_move = self.start_y_speed

        self.paddle_hits = 0