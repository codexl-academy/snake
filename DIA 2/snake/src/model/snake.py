"""Module with the representation of the Snake entity
along with some util classes such as Direction.
"""


from enum import Enum
from typing import List, Tuple


class Direction(Enum):
    """Enum class representing directions."""

    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3


class Snake:
    """Representation of the Snake entity."""

    def __init__(self, position: Tuple[int, int], direction: Direction, size: int):
        self.position = position
        self.direction = direction
        self.body = self._create_body(position, size)

    def _create_body(
        self, position: Tuple[int, int], size: int
    ) -> List[Tuple[int, int]]:
        """Generates the body of the snake starting from the
        position of the head. The body will be of size `size`
        and the snake will be placed horizontally, facing right.

        Args:
            position (Tuple[int, int]): The position of the head.
            size (int): Size of the snake.

        Returns:
            List[Tuple[int, int]]: Body of the snake, including the head.
        """
        body = [position]
        body.extend((body[i - 1][0] - 10, position[1]) for i in range(1, size))
        return body

    def move(self):
        """Updates the position of the head."""
        if self.direction == Direction.RIGHT:
            self.position = (self.position[0] + 10, self.position[1])
        elif self.direction == Direction.LEFT:
            self.position = (self.position[0] - 10, self.position[1])
        elif self.direction == Direction.UP:
            self.position = (self.position[0], self.position[1] - 10)
        else:
            self.position = (self.position[0], self.position[1] + 10)
        self._grow()

    def _grow(self):
        """Inserts the position of the head as the front position in the body."""
        self.body.insert(0, self.position)

    def trim(self):
        """Removes the tail of the body."""
        self.body.pop()

    def change_direction(self, new_direction: Direction):
        """Changes the direction of the snake in case the new direction
        is not opposite to the current direction.

        Args:
            new_direction (Direction): The candidate direction to change.
        """
        if not self._are_opposites(self.direction, new_direction):
            self.direction = new_direction

    def _are_opposites(self, direction1: Direction, direction2: Direction):
        return (
            (direction1 == Direction.RIGHT and direction2 == Direction.LEFT)
            or (direction1 == Direction.LEFT and direction2 == Direction.RIGHT)
            or (direction1 == Direction.UP and direction2 == Direction.DOWN)
            or (direction1 == Direction.DOWN and direction2 == Direction.UP)
        )
