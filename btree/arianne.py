class Arianne:

    _value: int
    _parent: 'Arianne'

    def __init__(self, value: int = 0):
        self._value = value
        self._parent = None

    def next(self, value: int) -> 'Arianne':
        child: 'Arianne' = Arianne(value)
        child._parent = self
        return child

    def parent(self) -> 'Arianne':
        return self._parent

    def get(self) -> int:
        return self._value