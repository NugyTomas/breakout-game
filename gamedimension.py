class GameDimension:

    def __init__(self, width, height):
        
        #Window
        self.window_width = int(width * 0.8)
        self.window_height = int(height * 0.8)

        #Countdown
        self.message_y = -self.window_height * 0.05
        
        #Walls
        self.left_wall = -(self.window_width / 2)
        self.right_wall = (self.window_width / 2)
        self.top_wall = (self.window_height / 2)
        self.bottom_wall = -(self.window_height / 2)
        
        #Scale
        scale = min(self.window_width, self.window_height)
        
        #Paddle
        self.paddle_start_x = 0
        self.paddle_bottom_margin = self.window_height * 0.08
        self.paddle_start_y = (self.bottom_wall + self.paddle_bottom_margin)
        self.paddle_width = scale * 0.24
        self.paddle_height = scale *  0.016
        
        #Ball
        self.ball_size = scale * 0.025
        self.ball_radius = self.ball_size / 2
        self.ball_start_x = 0
        ball_bottom_margin = self.window_height * 0.4
        self.ball_start_y = (self.bottom_wall + ball_bottom_margin)
        
        #Bricks
        brick_top_margin = self.window_height * 0.15
        self.brick_y = self.top_wall - brick_top_margin

        brick_x_margin = self.window_width * 0.075

        self.brick_spacing = scale * 0.005

        self.bricks_rows = 8
        self.bricks_cols = 14

        usable_width = (self.window_width - brick_x_margin * 2 - (self.bricks_cols - 1) * self.brick_spacing)
        self.brick_width = usable_width / self.bricks_cols

        self.brick_left_x = self.left_wall + brick_x_margin + self.brick_width/2

        bricks_area_height = self.window_height * 0.3
        usable_height = (bricks_area_height- (self.bricks_rows - 1) * self.brick_spacing)
        self.brick_height = usable_height / self.bricks_rows

        #Scoreboard
        self.scoreboard_font_size = max(12, int(scale * 0.025))
        scoreboard_top_margin = self.window_height * 0.06
        self.scoreboard_y = self.top_wall - scoreboard_top_margin
        self.high_score_y = int(self.top_wall - scoreboard_top_margin * 1.75)
        scoreboard_x_margin = self.window_width * 0.1
        self.scoreboard_left_x = self.left_wall + scoreboard_x_margin
        self.scoreboard_right_x = self.right_wall - scoreboard_x_margin

