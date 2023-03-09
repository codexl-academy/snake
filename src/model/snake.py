from typing import Tuple, List


class Snake:
    def __init__(self, position: Tuple[int, int], direction: str):
        self.position = position
        self.direction = direction
        self.body = self._create_body(position)

    def _create_body(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        body = [position]
        body.extend((body[i - 1][0] - 10, position[1]) for i in range(1, 4))
        return body

    def move(self):
        """Implement move to the direction stored in `direction`."""
        pass

    def update_body(self):
        """Implement update the body after every move."""
        pass

    def change_direction(self, new_direction: str):
        self.direction = new_direction
