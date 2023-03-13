"""Module that handles the Game entities.

As of now, it consist of a `Game` class handling the
main cycle and events of the game.
"""


import random
import sys
import time

import pygame

from model.fruit import Fruit
from model.snake import Direction, Snake
from renderer.render import Color, Renderer


class Game:
    """Class representing the Game entity."""

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.snake_speed = 15
        self.window_x = 720
        self.window_y = 480
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
        self.paused = False

    def _touch_boundaries(self) -> bool:
        """Checks whether the snake's head is touching the
        boundaries of the board.

        Returns:
            bool: True in case the snake's head is touching the boundaries, False otherwise.
        """
        return (
            self.snake.position[0] < 0
            or self.snake.position[0] > self.window_x - 10
            or self.snake.position[1] < 0
            or self.snake.position[1] > self.window_y - 10
        )

    def _touch_body(self) -> bool:
        """Checks wheter the snake's head is touching its body.

        Returns:
            bool: True in case the snake's head is touching its body, False otherwise.
        """
        return any(self.snake.position == block for block in self.snake.body[1:])

    def game_over(self):
        """Checks for the conditions of Game Over.

        The conditions are:
            * Snake's head touches boundaries.
            * Snake's head touches body.

        Returns:
            bool: True if any condition is met, False otherwise.
        """
        return self._touch_boundaries() or self._touch_body()

    def get_user_input(self):
        """Listens to KEYDOWN events to recognize
        direction changes.

        If no KEYDOWN event occurs, the direction doesn't change.

        Returns:
            Direction: The new direction of the snake.
        """
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
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        return change_to

    def _generate_fruit(self):
        """Generate new fruit."""
        self.fruit = Fruit(
            position=(
                random.randrange(1, (self.window_x // 10)) * 10,
                random.randrange(1, (self.window_y // 10)) * 10,
            )
        )

    def _increase_game_speed(self):
        self.snake_speed += 1

    def run(self):
        """Runs the main cycle of the Game."""
        while True:
            new_direction = self.get_user_input()

            if self.paused:
                continue

            self.snake.change_direction(new_direction)
            self.snake.move()

            if self.snake.position == self.fruit.position:
                self.score += 10
                self._generate_fruit()
                self._increase_game_speed()
            else:
                self.snake.trim()

            Renderer.render_game_state(
                self.snake.body,
                self.fruit.position,
                self.game_window,
                Color.GREEN.value,
                Color.WHITE.value,
                Color.BLACK.value,
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
                sys.exit()

            Renderer.render_score(
                self.score, self.game_window, Color.WHITE.value, "times new roman", 20
            )
            pygame.display.update()
            self.fps.tick(self.snake_speed)
