from turtle import Screen, Turtle
import time
from ball import Ball
from brickmanager import BrickManager
from gamedimension import GameDimension
from paddle import Paddle
from scoreboard import Scoreboard

def countdown():
    global counting

    counting = True

    for number in (3, 2, 1):
        message.clear()
        show_message(str(number),dimension.countdown_y,dimension.countdown_font)

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
    scoreboard.update_scoreboard()
    paddle.reset_position()
    countdown()

def toggle_pause():
    global game_paused

    if scoreboard.lives == 0:
        return

    if counting:
        return

    game_paused = not game_paused

    if game_paused:
        message.clear()
        show_message("⏸ PAUSED",dimension.game_state_y,dimension.game_state_font,)
    else:
        message.clear()

def game_loop():
    if game_paused:
        screen.ontimer(game_loop, 10)
        return

    screen.update()
    ball.move()

    # Detect collision with paddle
    horizontal_paddle_hit = (ball.right_edge >= paddle.left_edge and ball.left_edge <= paddle.right_edge)
    vertical_paddle_hit = (ball.bottom_edge <= paddle.top_edge and ball.top_edge >= paddle.bottom_edge)

    if ball.y_move < 0 and horizontal_paddle_hit and vertical_paddle_hit:
        offset = ball.xcor() - paddle.xcor()
        relative_hit = offset / (paddle.width / 2)
        ball.paddle_bounce(relative_hit)
        ball.paddle_hits += 1
        if ball.paddle_hits % 3 == 0:
            if abs(ball.x_move) <= 10:
                ball.x_move *= 1.05
            if abs(ball.y_move) <= 11:
                ball.y_move *= 1.05

    # Detect collision with walls
    if ball.left_edge <= dimension.left_wall or ball.right_edge >= dimension.right_wall:
        ball.x_bounce()

    if ball.top_edge >= dimension.top_wall:
        ball.y_bounce()

    # Detect collision with bottom wall
    if ball.top_edge <= dimension.bottom_wall:
        scoreboard.lives -= 1

        if scoreboard.lives > 0:
            reset_round()

        else:
            message.clear()

            # GAME OVER
            show_message("★ GAME OVER ★",dimension.game_state_y,dimension.game_state_font)

            show_message(
                f"Final Score: {scoreboard.current_score}\n"
                f"High Score: {max(scoreboard.current_score, scoreboard.record)}",
                dimension.final_score_y,
                dimension.final_score_font,
                "normal"
            )

            show_message("[Y] Play Again\n[N] Exit",dimension.retry_y ,dimension.retry_font)

            if scoreboard.current_score > scoreboard.record:
                scoreboard.write_new_record()

            return

    # Detect collision with bricks
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

            if len(brick_manager.bricks) == 0:
                paddle.next_level()
                scoreboard.level += 1
                brick_manager.build_bricks(dimension)
                reset_round()

            break

    screen.ontimer(game_loop, 10)

def retry_game():
    if scoreboard.lives > 0:
        return

    scoreboard.current_score = 0
    scoreboard.level = 1
    scoreboard.lives = 3
    scoreboard.record = scoreboard.get_current_record()

    for brick in brick_manager.bricks:
        brick.hideturtle()
    brick_manager.bricks.clear()

    brick_manager.build_bricks(dimension)

    reset_round()
    game_loop()

def exit_game():
    if scoreboard.lives > 0:
        return
    screen.bye()

# GLOBALS
game_paused = False
counting = False

screen = Screen()
screen.bgcolor("black")
screen.title("Breakout")

monitor_width = screen.cv._rootwindow.winfo_screenwidth()
monitor_height = screen.cv._rootwindow.winfo_screenheight()

dimension = GameDimension(monitor_width, monitor_height)

screen.setup(width=dimension.window_width, height=dimension.window_height)
screen.cv._rootwindow.resizable(False, False)
screen.tracer(0)

scoreboard = Scoreboard(dimension.scoreboard_y, dimension.scoreboard_font_size, dimension.scoreboard_left_x,
                        dimension.scoreboard_right_x, dimension.high_score_y)
paddle = Paddle(dimension.paddle_start_x, dimension.paddle_start_y, dimension.paddle_width, dimension.paddle_height)
ball = Ball(dimension.ball_start_x, dimension.ball_start_y, dimension.ball_radius)
brick_manager = BrickManager()
brick_manager.build_bricks(dimension)

screen.listen()

for key in ["a", "A", "Left"]:
    screen.onkeypress(paddle.go_left, key)

for key in ["d", "D", "Right"]:
    screen.onkeypress(paddle.go_right, key)

for key in ["space", "Escape"]:
    screen.onkeypress(toggle_pause, key)

for key in ["y", "Y"]:
    screen.onkeypress(retry_game, key)

for key in ["n", "N"]:
    screen.onkeypress(exit_game, key)

message = Turtle()
message.hideturtle()
message.penup()
message.color("white")

countdown()
game_loop()
screen.mainloop()
