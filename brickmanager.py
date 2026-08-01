from brick import Brick

COLORS = ["red", "orange", "green", "yellow", "blue", "purple"]
POINTS = [1,3,5,7,9,11]

class BrickManager:

    def __init__(self, dimension):

        self.bricks = []

        for row in range(dimension.bricks_rows):
            color_index = (row // 2)
            color = COLORS[color_index]
            for col in range(dimension.bricks_cols):
                x = dimension.brick_left_x + (dimension.brick_width + dimension.brick_spacing) * col
                y = dimension.brick_y - (dimension.brick_height + dimension.brick_spacing) * row
                brick = Brick(x,y,dimension.brick_width,dimension.brick_height, color)
                self.bricks.append(brick)


