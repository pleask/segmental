import unittest
import numpy as np
from numpy.testing import assert_array_equal
from .segment import Segment, SegmentCollection

class TestSegment(unittest.TestCase):
    def test_as_array(self):
        array = np.zeros(1)
        segment = Segment(array)
        self.assertEqual(array, segment)

    def test_addition(self):
        segment = Segment(np.ones(1)) + 2
        array = np.ones(1) + 2
        assert_array_equal(array, segment)

    def test_multiplication(self):
        segment = Segment(np.int_([1, 0]))
        assert_array_equal(np.int_([5, 0]), segment * np.int_([5,1]))
        

class TestSegmentCollection(unittest.TestCase):
    def test_init(self):
        segments = [np.zeros(1), np.zeros(1)]
        segment_collection = SegmentCollection(segments)
        assert_array_equal(segments, segment_collection.segments)


if __name__ == "__main__":
    unittest.main()
