import unittest
import numpy as np
from .segment import Segment, SegmentCollection


class TestSegment(unittest.TestCase):
    def test_as_array(self):
        array = np.zeros(1)
        segment = Segment(array)
        self.assertEqual(array, segment)


class TestSegmentCollection(unittest.TestCase):
    def test_init(self):
        segments = [np.zeros(1), np.zeros(1)]
        segment_collection = SegmentCollection(segments)
        self.assertEqual(segments, segment_collection.segments)

if __name__ == "__main__":
    unittest.main()
