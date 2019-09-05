import unittest
import numpy as np
from .segments import Segments


class TestSegments(unittest.TestCase):
    def test_as_array(self):
        array = np.zeros(1)
        segments = Segments(array)
        self.assertEqual(array, segments)

if __name__ == "__main__":
    unittest.main()
