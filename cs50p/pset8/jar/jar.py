class Jar:
    def __init__(self, capacity=12)
        self.capacity = capacity
        self.size = size

    def __str__(self):
        for _ in self.capacity:
            print("🍪", end="")
        print()

    def deposit(self, n):
        new_size = n + self._size
        if new_size > self.capacity:
            raise ValueError("Capacity exceeded")
        self._size = new_size

    def withdraw(self, n):
        remaining = self._size - n
        if n > self._size:
            raise ValueError("Not enough cookies")

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
        ...


jar = Jar()

