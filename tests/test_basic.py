#!/usr/bin/python3

import unittest
from vector import VectorHelper


class VectorHelperTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_somme(self):
        """
        Tests if 'somme' method works properly
        """
        vector1 = VectorHelper("1 3 -1 6 -7 0.7")
        vector2 = VectorHelper("0 6 7 2 7 -7")

        self.assertEqual(vector1.somme(vector2), [1.0, 9.0, 6.0, 8.0, 0.0, -6.3])

    def test_inverse(self):
        vector = VectorHelper("1 3 -1 6 -7 0.7")

        expected = list(map(float, "1 3 -1 6 -7 0.7".split()[::-1]))
        self.assertEqual(vector.inverse(), expected)

    def test_size(self):
        vector = VectorHelper("1 3 -1 6 -7 0.7")
        expected_size = 6
        self.assertEqual(vector.size, expected_size)

    def test_minmax(self):
        expected = (-7.0, 6)
        vector = VectorHelper("1 3 -1 6 -7 0.7")
        self.assertEqual(vector.MinMax(), expected)

    def test_sort(self):
        expected = [-7.0, -1.0, 0.7, 1.0, 3.0, 6.0]
        vector = VectorHelper("1 3 -1 6 -7 0.7")
        vector.sort()
        self.assertEqual(vector.get_elements, expected)


if __name__ == "__main__":
    unittest.main()