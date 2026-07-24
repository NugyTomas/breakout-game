
class GameDimension:

    def __init__(self, width, height):
        self.window_width = int(width * 0.8)
        self.window_height = int(height * 0.8)

        self.left_wall = -(self.window_width / 2)
        self.right_wall = (self.window_width / 2)
        self.top_wall = (self.window_height / 2)
        self.bottom_wall = -(self.window_height / 2)

        self.brick_width = self.window_width / 15
        self.brick_height = self.window_height / 20   #tohle je jen nastrel, upravim pak podle vizualniho pocitu

        self.scale = min(self.window_width, self.window_height)

        self.paddle_start_x = 0
        self.paddle_bottom_margin = self.window_height * 0.08
        self.paddle_start_y = (self.bottom_wall + self.paddle_bottom_margin)
        self.paddle_width = self.scale *  0.0008
        self.paddle_height = self.scale * 0.012

        self.ball_size = self.scale * 0.025
        self.ball_radius = self.ball_size / 2
