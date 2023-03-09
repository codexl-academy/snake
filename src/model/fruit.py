from typing import Tuple


class Fruit:
    """Representation of the Fruit entity.

    Probably best to use `dataclass` here.
    """

    def __init__(self, position: Tuple[int, int]):
        self.position = position
