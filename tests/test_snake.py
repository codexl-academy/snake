from unittest import TestCase
from src.model.snake import Snake


class TestSnake(TestCase):
    def setUp(self):
        self.snake = Snake(position=(50, 50), direction="R")

    def test_create_body(self):
        self.assertEqual(self.snake.body, [(50, 50), (40, 50), (30, 50), (20, 50)])
