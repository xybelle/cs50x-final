class Jar:
    def __init__(self, capacity=12)
        self.capacity = capacity

    def __str__(self):
        for _ in self._size:
            print("🍪", end="")
        print()

    def deposit(self, n):
        new_size = n + self._size
        if new_size > self.capacity:
            raise ValueError("Capacity exceeded")
        self.size = new_size

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Not enough cookies")
        remaining = self._size - n
        self.size = remaining

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size=0):
        self._size = size


jar = Jar()

