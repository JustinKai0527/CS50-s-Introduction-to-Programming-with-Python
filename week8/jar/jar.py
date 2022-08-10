class Jar:
    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError
        self._capacity = capacity
        self._n = 0

    def __str__(self):
        return ("🍪"*self._n)

    def deposit(self, n):
        if n + self._n > self._capacity:
            raise ValueError

        self._n += n

    def withdraw(self, n):

        if self._n - n < 0:
            raise ValueError

        self._n -= n


    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self,n):
        self._capacity = n


    @property
    def size(self):
        return self._n
    @size.setter
    def size(self,n):
        self._n = n
