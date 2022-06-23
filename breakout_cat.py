from turtle import Screen
from ball import Ball
from block import Block
from paddle import Paddle
import time

from scoreboard import Scoreboard


class BreakoutCat():
    def __init__(self):
        self.scoreboard = None
        self.blocks = None
        self.paddle = None
        self.ball = None
        self.screen: Screen = None
        self.game_is_on = True
        self.initial_ui()
        # close turtle when close window
        self.screen._root.protocol("WM_DELETE_WINDOW", self.stop)

    def initial_ui(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=800)
        self.screen.bgcolor('black')
        self.screen.tracer(0)
        self.screen.title('Breakout Cat')
        self.ball = Ball()
        self.paddle = Paddle((0, -350))
        self.blocks = []
        self.build_blocks()
        self.scoreboard = Scoreboard(len(self.blocks))

        self.screen.listen()
        self.screen.onkey(self.paddle.go_left, "Left")
        self.screen.onkey(self.paddle.go_right, "Right")
        self.screen.onkey(self.stop, "q")

    def build_blocks(self):
        for x in range(-260, 261, 65):
            for y in range(100, 351, 15):
                self.blocks.append(Block(x - 5, y))

    def run(self):
        while self.game_is_on:
            time.sleep(self.ball.move_speed)
            self.ball.move()
            self.screen.update()
            # Detect collision with wall
            x_limit = 300
            y_limit = 340
            if self.ball.xcor() > x_limit or self.ball.xcor() < -x_limit:
                self.ball.bounce_x()
            if self.ball.ycor() > y_limit:
                self.ball.bounce_y()
            # Detect collision with below_paddle
            if (-360 <= self.ball.ycor() <= -340) and (
                    self.paddle.xcor() - 70 < self.ball.xcor() < self.paddle.xcor() + 70) and self.ball.y_move > 0:
                self.ball.bounce_y()
            # Detect below paddle misses
            if self.ball.ycor() < -400:
                self.ball.reset_position()

            # Detect collision with blocks
            for block in self.blocks:
                if (block.xcor() - 50 < self.ball.xcor() < block.xcor() + 50) and (
                        block.ycor() - 10 < self.ball.ycor() < block.ycor() + 10):
                    block.goto(2000, 2000)
                    self.blocks.remove(block)
                    self.ball.bounce_y()
                    self.scoreboard.point()
        self.screen.bye()

    def stop(self):
        self.game_is_on = False
