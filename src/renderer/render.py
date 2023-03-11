from enum import Enum

import pygame


class Color(Enum):
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(255, 0, 0)
    GREEN = pygame.Color(0, 255, 0)


class Renderer:
    @staticmethod
    def render_score(
        score: int, game_window, color: Color, font: str, font_size: int
    ) -> None:

        score_font = pygame.font.SysFont(font, font_size)
        score_surface = score_font.render(f"Score : {score}", True, color)
        score_rect = score_surface.get_rect()
        game_window.blit(score_surface, score_rect)

    @staticmethod
    def render_game_over(
        score: int,
        game_window,
        window_x,
        window_y,
        color: Color,
        font: str,
        font_size: int,
    ) -> None:

        my_font = pygame.font.SysFont(font, font_size)
        game_over_surface = my_font.render(f"Your Score is : {score}", True, color)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x / 2, window_y / 4)
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()

    @staticmethod
    def render_game_state(
        snake, fruit, game_window, snake_color: Color, fruit_color: Color
    ) -> None:
        for pos in snake.body:
            pygame.draw.rect(
                game_window, snake_color, pygame.Rect(pos[0], pos[1], 10, 10)
            )
        pygame.draw.rect(
            game_window,
            fruit_color,
            pygame.Rect(fruit.position[0], fruit.position[1], 10, 10),
        )
