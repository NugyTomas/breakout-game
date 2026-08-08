from screeninfo import get_monitors
from turtle import Screen, Turtle
import time
from ball import Ball
from brickmanager import BrickManager
from gamedimension import GameDimension
from paddle import Paddle
from scoreboard import Scoreboard

# -----------------------------------------------------
# Globals / Constants
# -----------------------------------------------------

MOVE_LEFT_KEYS = ("a", "A", "Left")
MOVE_RIGHT_KEYS = ("d", "D", "Right")
PAUSE_KEYS = ("space", "Escape")
RETRY_GAME_KEYS = ("y", "Y")
EXIT_GAME_KEYS = ("n", "N")

game_paused = False
counting = False

# -----------------------------------------------------
# Helper functions
# -----------------------------------------------------

def countdown():
    global counting

    counting = True

    for number in (3, 2, 1):
        message.clear()
        show_message(str(number),dimension.countdown_y,dimension.countdown_font_size)

        screen.update()
        time.sleep(1)

    message.clear()
    screen.update()

    counting = False

def show_message(text, y, size, style="bold"):
    message.goto(0, y)
    message.write(
        text,
        align="center",
        font=("Courier", size, style)
    )

def reset_round():
    ball.reset()
    paddle.reset_position()
    countdown()

# -----------------------------------------------------
# Collision detection
# -----------------------------------------------------

def detect_paddle_collision():
    horizontal_paddle_hit = ball.right_edge >= paddle.left_edge and ball.left_edge <= paddle.right_edge
    vertical_paddle_hit = ball.bottom_edge <= paddle.top_edge and ball.top_edge >= paddle.bottom_edge
    moving_down = ball.y_move < 0

    if moving_down and horizontal_paddle_hit and vertical_paddle_hit:
        hit_offset = ball.xcor() - paddle.xcor()
        relative_hit = hit_offset / (paddle.width / 2)
        ball.paddle_bounce(relative_hit)
        ball.paddle_hits += 1

        if ball.paddle_hits % 3 == 0:
            ball.x_move *= 1.1
            ball.y_move *= 1.1
            ball.limit_speed()

def detect_wall_collisions():
    if ball.left_edge <= dimension.left_wall or ball.right_edge >= dimension.right_wall:
        ball.x_bounce()

    if ball.top_edge >= dimension.top_wall:
        ball.y_bounce()

def check_bottom_collision():
    if ball.top_edge <= dimension.bottom_wall:
        scoreboard.lives -= 1
        scoreboard.update_scoreboard()

        if scoreboard.lives > 0:
            reset_round()
            return False

        message.clear()

        # GAME OVER
        show_message("★ GAME OVER ★",dimension.game_state_y,dimension.game_state_font_size)

        show_message(
            f"Final Score: {scoreboard.current_score}\n"
            f"High Score: {max(scoreboard.current_score, scoreboard.record)}",
            dimension.final_score_y,
            dimension.final_score_font_size,
            "normal"
            )

        show_message("[Y] Play Again\n[N] Exit",dimension.retry_y ,dimension.retry_font_size)

        if scoreboard.current_score > scoreboard.record:
            scoreboard.write_new_record()

        return True

    return False

def detect_brick_collision():
    for brick in brick_manager.bricks:
        vertical_brick_hit = (ball.top_edge >= brick.bottom_edge and ball.bottom_edge <= brick.top_edge)
        horizontal_brick_hit = (ball.right_edge >= brick.left_edge and ball.left_edge <= brick.right_edge)

        if vertical_brick_hit and horizontal_brick_hit:
            left_overlap = ball.right_edge - brick.left_edge
            right_overlap = brick.right_edge - ball.left_edge
            top_overlap = brick.top_edge - ball.bottom_edge
            bottom_overlap = ball.top_edge - brick.bottom_edge

            min_overlap = min(left_overlap, right_overlap, top_overlap, bottom_overlap)

            if min_overlap == left_overlap or min_overlap == right_overlap:
                ball.x_bounce()
                ball.setx(ball.xcor() + ball.x_move)

            elif min_overlap == top_overlap or min_overlap == bottom_overlap:
                ball.y_bounce()
                ball.sety(ball.ycor() + ball.y_move)

            scoreboard.current_score += brick.point
            scoreboard.update_scoreboard()
            brick.hideturtle()
            brick_manager.bricks.remove(brick)

            if not brick_manager.bricks:
                next_level()

            break

# -----------------------------------------------------
# Game logic
# -----------------------------------------------------

def move_left():
    if counting or game_paused:
        return

    paddle.go_left(dimension)

def move_right():
    if counting or game_paused:
        return

    paddle.go_right(dimension)

def toggle_pause():
    global game_paused

    if counting or scoreboard.lives == 0:
        return

    game_paused = not game_paused

    if game_paused:
        message.clear()
        show_message("⏸ PAUSED",dimension.game_state_y,dimension.game_state_font_size,)
    else:
        message.clear()

def next_level():
    paddle.next_level()

    if scoreboard.lives < 3:
        scoreboard.lives += 1

    scoreboard.level += 1
    scoreboard.update_scoreboard()

    brick_manager.build_bricks(dimension)
    reset_round()

def retry_game():
    if scoreboard.lives > 0:
        return

    scoreboard.reset()

    brick_manager.clear()
    brick_manager.build_bricks(dimension)

    reset_round()
    game_loop()

def exit_game():
    if scoreboard.lives > 0:
        return

    screen.bye()

def game_loop():
    if game_paused:
        screen.ontimer(game_loop, 15)
        return

    screen.update()

    ball.move()

    detect_paddle_collision()
    detect_wall_collisions()

    if check_bottom_collision():
        return

    detect_brick_collision()

    # Schedule next frame
    screen.ontimer(game_loop, 15)

# -----------------------------------------------------
# Game initialization
# -----------------------------------------------------

def get_primary_monitor_size():
    monitors = get_monitors()

    monitor = next((m for m in monitors if m.is_primary),monitors[0])

    return monitor.width, monitor.height

screen = Screen()
screen.bgcolor("black")
screen.title("Breakout")

monitor_width, monitor_height = get_primary_monitor_size()

dimension = GameDimension(monitor_width, monitor_height)

screen.setup(width=dimension.window_width, height=dimension.window_height)
screen.cv._rootwindow.resizable(False, False)
screen.tracer(0)

scoreboard = Scoreboard(dimension)
paddle = Paddle(dimension)
ball = Ball(dimension)

brick_manager = BrickManager()
brick_manager.build_bricks(dimension)

# -----------------------------------------------------
# Controls
# -----------------------------------------------------

screen.listen()

for key in MOVE_LEFT_KEYS:
    screen.onkeypress(move_left, key)

for key in MOVE_RIGHT_KEYS:
    screen.onkeypress(move_right, key)

for key in PAUSE_KEYS:
    screen.onkeypress(toggle_pause, key)

for key in RETRY_GAME_KEYS:
    screen.onkeypress(retry_game, key)

for key in EXIT_GAME_KEYS:
    screen.onkeypress(exit_game, key)


# -----------------------------------------------------
# Message turtle
# -----------------------------------------------------

message = Turtle()
message.hideturtle()
message.penup()
message.color("white")

# -----------------------------------------------------
# Game
# -----------------------------------------------------

countdown()
game_loop()

screen.mainloop()
