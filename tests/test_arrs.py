import unittest

from utils.arrs import get
from utils.arrs import my_slice


class TestGet(unittest.TestCase):
    def test_get(self):
        self.assertEqual(get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(get([], 0, "test"), "test")
        self.assertEqual(get([1, 5, 3], 1, "test"), 5)
        self.assertEqual(get([1, 2, 3], 2, "test"), 3)
        self.assertEqual(get([1, 2, 3], -1, "test"), "test")

    def test_slice(self):
        self.assertEqual(my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(my_slice([1, 2, 3], -1), [3])
        self.assertEqual(my_slice([1, 2, 3], 0), [1, 2, 3])
        self.assertEqual(my_slice([1, 2, 3, 4], -2), [3, 4])
        self.assertEqual(my_slice([1, 2, 3, 4], -1, 3), [])
        self.assertEqual(my_slice([], 0), [])
        self.assertEqual(my_slice([1, 2, 3, 4], -6), [1, 2, 3, 4])
        self.assertEqual(my_slice([1, 2, 3, 4], -1, -2), [])
