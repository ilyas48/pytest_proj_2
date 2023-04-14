import unittest

from utils.arrs import get


class TestGet(unittest.TestCase):
    def test_get(self):
        self.assertEqual(get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(get([1, 5, 3], 1, "test"), 5)
        self.assertEqual(get([1, 2, 3], 2, "test"), 3)
        self.assertEqual(get([1, 2, 3], -1, 3), 3)


    def test_slice(self):
        self.assertEqual(get([1, 2, 3, 4], 1, 3), 2, 3)
        self.assertEqual(get([1, 2, 3], 1), 2, 3)


if __name__ == '__main__':
