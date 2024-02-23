class Jar:
    def __init__(self, capacity=12)
        self.capacity = capacity
        self.size = size

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

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

