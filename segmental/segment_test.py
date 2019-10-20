import unittest
import numpy as np
from .segments import Segments


class TestSegment(unittest.TestCase):
    def test_as_array(self):
        array = np.zeros(1)
        segment = Segment(array)
        self.assertEqual(array, segment)

if __name__ == "__main__":
    unittest.main()
