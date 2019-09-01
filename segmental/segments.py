class Segments:
    def __init__(self, arr):
        self._arr = arr

    def __array__(self):
        return self._arr
