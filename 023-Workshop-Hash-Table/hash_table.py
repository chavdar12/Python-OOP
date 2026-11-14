class HashTable:
    """Open-addressing hash table (linear probing) that doubles its array when it gets full."""

    def __init__(self):
        self.array = [None] * 4
        self._count = 0

    def hash(self, key: str) -> int:
        index = sum(ord(ch) for ch in key) % len(self.array)
        while self.array[index] is not None and self.array[index][0] != key:
            index = (index + 1) % len(self.array)
        return index

    def add(self, key: str, value):
        index = self.hash(key)
        if self.array[index] is None:
            self._count += 1
        self.array[index] = (key, value)
        if self._count == len(self.array):
            self._resize()

    def get(self, key: str):
        slot = self.array[self.hash(key)]
        if slot is None:
            raise KeyError(key)
        return slot[1]

    def _resize(self):
        items = [slot for slot in self.array if slot is not None]
        self.array = [None] * (len(self.array) * 2)
        self._count = 0
        for key, value in items:
            self.add(key, value)

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __len__(self):
        # The task's example prints 4 for two entries: len() is the array capacity.
        return len(self.array)
