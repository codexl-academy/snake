from dataclasses import dataclass
from typing import Tuple


@dataclass
class Fruit:
    """Representation of the Fruit entity."""

    position: Tuple[int, int]
