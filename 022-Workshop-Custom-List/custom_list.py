class CustomList:
    """A list-like structure built on top of a plain Python list, without inheriting from it."""

    def __init__(self, *values):
        self._values = list(values)

    def append(self, value):
        self._values.append(value)
        return self._values

    def remove(self, index):
        self._check_index(index)
        return self._values.pop(index)

    def get(self, index):
        self._check_index(index)
        return self._values[index]

    def extend(self, iterable):
        self._values.extend(iterable)
        return self._values

    def insert(self, index, value):
        self._values.insert(index, value)
        return self._values

    def pop(self):
        if not self._values:
            raise IndexError("pop from empty list")
        return self._values.pop()

    def clear(self):
        self._values.clear()

    def index(self, value):
        return self._values.index(value)

    def count(self, value):
        return self._values.count(value)

    def reverse(self):
        return self._values[::-1]

    def copy(self):
        return self._values.copy()

    def size(self):
        return len(self._values)

    def add_first(self, value):
        self._values.insert(0, value)

    def dictionize(self):
        values = self._values + [" "] * (len(self._values) % 2)
        return {values[i]: values[i + 1] for i in range(0, len(values), 2)}

    def move(self, amount):
        if amount < 0 or amount > len(self._values):
            raise ValueError("Invalid amount")
        self._values = self._values[amount:] + self._values[:amount]
        return self._values

    def sum(self):
        return sum(self._weight(v) for v in self._values)

    def overbound(self):
        return self._extreme_index(max)

    def underbound(self):
        return self._extreme_index(min)

    def _extreme_index(self, pick):
        if not self._values:
            raise ValueError("The list is empty")
        weights = [self._weight(v) for v in self._values]
        return weights.index(pick(weights))

    @staticmethod
    def _weight(value):
        return value if isinstance(value, (int, float)) else len(value)

    def _check_index(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if not -len(self._values) <= index < len(self._values):
            raise IndexError("Index out of range")
