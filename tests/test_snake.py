from unittest import TestCase
from src.model.snake import Direction, Snake


class TestSnake(TestCase):
    def setUp(self):
        self.snake = Snake(position=(50, 50), direction=Direction.RIGHT)

    def test_create_body(self):
        self.assertEqual(self.snake.body, [(50, 50), (40, 50), (30, 50), (20, 50)])

    def test_move(self):
        self.snake.move()
        self.assertEqual(self.snake.position, (60, 50))
        self.assertEqual(self.snake.body, [(60, 50), (50, 50), (40, 50), (30, 50)])

    def test_change_direction(self):
        self.snake.change_direction(Direction.UP)
        self.assertEqual(self.snake.direction, Direction.UP)

    def test_change_direction_opposite(self):
        self.snake.change_direction(Direction.LEFT)
        self.assertEqual(self.snake.direction, Direction.RIGHT)
