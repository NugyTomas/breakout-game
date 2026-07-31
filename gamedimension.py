class GameDimension:

    def __init__(self, width, height):
        self.window_width = int(width * 0.8)
        self.window_height = int(height * 0.8)

        self.left_wall = -(self.window_width / 2)
        self.right_wall = (self.window_width / 2)
        self.top_wall = (self.window_height / 2)
        self.bottom_wall = -(self.window_height / 2)

        self.brick_width = self.window_width / 15
        self.brick_height = self.window_height / 20

        self.scale = min(self.window_width, self.window_height)

        self.paddle_start_x = 0
        self.paddle_bottom_margin = self.window_height * 0.08
        self.paddle_start_y = (self.bottom_wall + self.paddle_bottom_margin)
        self.paddle_width = self.scale * 0.24
        self.paddle_height = self.scale *  0.016

        self.ball_size = self.scale * 0.025
        self.ball_radius = self.ball_size / 2
        self.ball_start_x = 0
        self.ball_bottom_margin = self.window_height * 0.4
        self.ball_start_y = (self.bottom_wall + self.ball_bottom_margin)

        self.scoreboard_font_size = max(12, int(self.scale * 0.025))
        self.scoreboard_top_margin = self.window_height * 0.06
        self.scoreboard_y = self.top_wall - self.scoreboard_top_margin
        self.high_score_y = int(self.top_wall - self.scoreboard_top_margin * 1.75)
        self.x_margin = self.window_width * 0.1
        self.left_x = self.left_wall + self.x_margin
        self.right_x = self.right_wall - self.x_margin


