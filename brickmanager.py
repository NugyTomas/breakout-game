from brick import Brick

BRICKS = (
    ("yellow", 7),
    ("green", 5),
    ("blue", 3),
    ("purple", 1),
)

class BrickManager:

    def __init__(self):
        self.bricks = []

    def build_bricks(self, dimension):
        for row in range(dimension.bricks_rows):
            color_index = (row // 2)
            color, points = BRICKS[color_index]
            for col in range(dimension.bricks_cols):
                x = dimension.brick_left_x + (dimension.brick_width + dimension.brick_spacing) * col
                y = dimension.brick_y - (dimension.brick_height + dimension.brick_spacing) * row
                brick = Brick(x,y,dimension.brick_width,dimension.brick_height, color, points)
                self.bricks.append(brick)


