"""Module that handles the rendering of the components and states of the game.

As of now, it handles the rendering of:

    * The Score.
    * The Game Over screen.
    * The Current State of the Game.
"""


from enum import Enum
from typing import List, Tuple

import pygame


class Color(Enum):
    """Enum representing the colors to be used in the game.

    Values are represented as RGB vectors.
    """

    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(255, 0, 0)
    GREEN = pygame.Color(0, 255, 0)


class Renderer:
    """Class that handles the rendering of the components and states of the Game."""

    @staticmethod
    def render_score(
        score: int, game_window, color: Color, font: str, font_size: int
    ):
        """Renders the score on the top left corner of the screen.

        Args:
            score (int): The score of the Game.
            game_window (pygame.display): The window where the Game is being displayed.
            color (Color): Color of the font.
            font (str): Style of the font.
            font_size (int): Size of the font.
        """
        score_font = pygame.font.SysFont(font, font_size)
        score_surface = score_font.render(f"Score : {score}", True, color)
        score_rect = score_surface.get_rect()
        game_window.blit(score_surface, score_rect)

    @staticmethod
    def render_game_over(
        score: int,
        game_window,
        window_x: int,
        window_y: int,
        color: Color,
        font: str,
        font_size: int,
    ):
        """Renders the `Game Over` state.

        Red-colored sign with the score in the middle of the screen.

        Args:
            score (int): The score of the Game.
            game_window (pygame.display): The window where the Game is being displayed.
            window_x (int): Dimension `x` of the window.
            window_y (int): Dimension `y` of the window.
            color (Color): Color of the font.
            font (str): Style of the font.
            font_size (int): Size of the font.
        """
        my_font = pygame.font.SysFont(font, font_size)
        game_over_surface = my_font.render(f"Your Score is : {score}", True, color)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x / 2, window_y / 4)
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()

    @staticmethod
    def render_game_state(
        snake_body: List[Tuple[int, int]],
        fruit_position: Tuple[int, int],
        game_window,
        snake_color: Color,
        fruit_color: Color,
        window_color: Color,
    ):
        """Renders the state of the Game.

        Handles the rendering of the Snake and the Fruit.

        Args:
            snake_body (List[Tuple[int, int]]): List of positions of the snake's body.
            fruit_position (Tuple[int, int]): Position of the fruit.
            game_window (pygame.display): The window where the Game is being displayed.
            snake_color (Color): Color of the snake.
            fruit_color (Color): Color of the fruit.
            window_color (Color): Color of the window.
        """
        game_window.fill(window_color)
        for pos in snake_body:
            pygame.draw.rect(
                game_window, snake_color, pygame.Rect(pos[0], pos[1], 10, 10)
            )
        pygame.draw.rect(
            game_window,
            fruit_color,
            pygame.Rect(fruit_position[0], fruit_position[1], 10, 10),
        )
