import random
import time

import pygame

from model.fruit import Fruit
from model.snake import Direction, Snake
from renderer.render import Color, Renderer


class Game:

    snake_speed = 15

    # Window size
    window_x = 720
    window_y = 480

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.game_window = pygame.display.set_mode((self.window_x, self.window_y))
        self.fps = pygame.time.Clock()

        self.snake = Snake(position=(100, 50), direction=Direction.RIGHT, size=4)
        self.fruit = Fruit(
            position=(
                random.randrange(1, (self.window_x // 10)) * 10,
                random.randrange(1, (self.window_y // 10)) * 10,
            )
        )
        self.score = 0
        self.fruit_spawn = True

    def touch_boundaries(self) -> bool:
        return (
            self.snake.position[0] < 0
            or self.snake.position[0] > self.window_x - 10
            or self.snake.position[1] < 0
            or self.snake.position[1] > self.window_y - 10
        )

    def touch_body(self) -> bool:
        return any(self.snake.position == block for block in self.snake.body[1:])

    def game_over(self):
        return self.touch_boundaries() or self.touch_body()

    def get_next_direction(self):
        change_to = self.snake.direction
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = Direction.UP
                if event.key == pygame.K_DOWN:
                    change_to = Direction.DOWN
                if event.key == pygame.K_LEFT:
                    change_to = Direction.LEFT
                if event.key == pygame.K_RIGHT:
                    change_to = Direction.RIGHT
        return change_to

    def run(self):
        while True:

            self.snake.change_direction(self.get_next_direction())
            self.snake.move()

            if self.snake.position == self.fruit.position:
                self.score += 10
                self.fruit_spawn = False
            else:
                self.snake.trim()

            if not self.fruit_spawn:
                self.fruit = Fruit(
                    position=(
                        random.randrange(1, (self.window_x // 10)) * 10,
                        random.randrange(1, (self.window_y // 10)) * 10,
                    )
                )

            self.fruit_spawn = True
            self.game_window.fill(Color.BLACK.value)

            Renderer.render_game_state(
                self.snake,
                self.fruit,
                self.game_window,
                Color.GREEN.value,
                Color.WHITE.value,
            )

            if self.game_over():
                Renderer.render_game_over(
                    self.score,
                    self.game_window,
                    self.window_x,
                    self.window_y,
                    Color.RED.value,
                    "times new roman",
                    50,
                )
                time.sleep(2)
                pygame.quit()
                quit()

            Renderer.render_score(
                self.score, self.game_window, Color.WHITE.value, "times new roman", 20
            )
            pygame.display.update()
            self.fps.tick(self.snake_speed)
