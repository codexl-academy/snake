from unittest import TestCase

from src.model.fruit import Fruit


class TestFruit(TestCase):
    def setUp(self):
        self.fruit = Fruit((10, 10))

    def test_created_as_dataclass(self):
        self.assertEqual(self.fruit.position, (10, 10))
