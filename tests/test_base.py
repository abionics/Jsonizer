import unittest

from examples.example_hints import Egg, Bird, json_data
from jsonizer import Jsonizer


class TestBase(unittest.TestCase):

    def test_nested(self):
        parser = Jsonizer(Bird, Egg)
        bird = parser.parse(json_data)
        self._assert_bird(bird)

    def test_file(self):
        parser = Jsonizer(Bird, Egg)
        bird = parser.parse_file('../examples/bird.json')
        self._assert_bird(bird)

    def _assert_bird(self, bird: Bird):
        self.assertEqual(
            str(bird), 'Bird "Duck" with eggs [white egg with size 12, purple egg with size 69]', 'Wrong parsing'
        )
        self.assertEqual(bird._eggs[1]._color, 'purple', 'Wrong parsing')
