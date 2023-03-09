from typing import Tuple, List
from enum import Enum


class Direction(Enum):
    """Enum class representing directions."""

    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3


class Snake:
    """Representation of the Snake entity."""

    def __init__(self, position: Tuple[int, int], direction: Direction):
        self.position = position
        self.direction = direction
        self.body = self._create_body(position)

    def _create_body(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        body = [position]
        body.extend((body[i - 1][0] - 10, position[1]) for i in range(1, 4))
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
        self._update_body()

    def _update_body(self):
        """Updates the positions of the body

        This method can change when we take fruits into consideration.
        """
        self.body.insert(0, self.position)
        self.body.pop()

    def grow(self):
        """Implement grow body after eating fruit."""
        pass

    def change_direction(self, new_direction: Direction):
        if not self._are_opposites(self.direction, new_direction):
            self.direction = new_direction

    def _are_opposites(self, direction1: Direction, direction2: Direction):
        return (
            (direction1 == Direction.RIGHT and direction2 == Direction.LEFT)
            or (direction1 == Direction.LEFT and direction2 == Direction.RIGHT)
            or (direction1 == Direction.UP and direction2 == Direction.DOWN)
            or (direction1 == Direction.DOWN and direction2 == Direction.UP)
        )
