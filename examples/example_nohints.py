from jsonizer import Jsonizer


class Egg:
    def __init__(self, size, color='white'):
        self._size = size
        self._color = color

    def __repr__(self):
        return f'{self._color} egg with size {self._size}'


class Bird:
    def __init__(self, name, eggs):
        self._name = name
        self._eggs = eggs

    def __repr__(self):
        return f'Bird "{self._name}" with eggs {self._eggs}'


json_data = {
    'name': 'Duck',
    'eggs': [{
        'size': 12,
    }, {
        'size': 69,
        'color': 'purple',
    }]
}

if __name__ == '__main__':
    parser = Jsonizer(Bird, Egg)
    bird = parser.parse(json_data)
    print(bird)
