from jsonizer import Jsonizer


class Egg:
    def __init__(self, size: int, color: str = 'white'):
        self._size = size
        self._color = color

    def __repr__(self) -> str:
        return f'{self._color} egg with size {self._size}'


class Bird:
    def __init__(self, name: str, eggs: list[Egg]):
        self._name = name
        self._eggs = eggs

    def __repr__(self) -> str:
        return f'Bird "{self._name}" with eggs {self._eggs}'


parser = Jsonizer(Bird, Egg)
bird = parser.parse_file('bird.json')
print(bird)
