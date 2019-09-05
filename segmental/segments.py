import numpy as np

class Segments:
    def __init__(self, arr: np.ndarray):
        self._arr = arr

    def __array__(self) -> np.ndarray:
        return self._arr
